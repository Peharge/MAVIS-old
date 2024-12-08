# Englisch | Peharge: This source code is released under the MIT License.
#
# Usage Rights:
# The source code may be copied, modified, and adapted to individual requirements.
# Users are permitted to use this code in their own projects, both for private and commercial purposes.
# However, it is recommended to modify the code only if you have sufficient programming knowledge,
# as changes could cause unintended errors or security risks.
#
# Dependencies and Additional Frameworks:
# The code relies on the use of various frameworks and executes additional files.
# Some of these files may automatically install further dependencies required for functionality.
# It is strongly recommended to perform installation and configuration in an isolated environment
# (e.g., a virtual environment) to avoid potential conflicts with existing software installations.
#
# Disclaimer:
# Use of the code is entirely at your own risk.
# Peharge assumes no liability for damages, data loss, system errors, or other issues
# that may arise directly or indirectly from the use, modification, or redistribution of the code.
#
# Please read the full terms of the MIT License to familiarize yourself with your rights and obligations.

# Deutsch | Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.
#
# Nutzungsrechte:
# Der Quellcode darf kopiert, bearbeitet und an individuelle Anforderungen angepasst werden.
# Nutzer sind berechtigt, diesen Code in eigenen Projekten zu verwenden, sowohl für private als auch kommerzielle Zwecke.
# Es wird jedoch empfohlen, den Code nur dann anzupassen, wenn Sie über ausreichende Programmierkenntnisse verfügen,
# da Änderungen unbeabsichtigte Fehler oder Sicherheitsrisiken verursachen könnten.
#
# Abhängigkeiten und zusätzliche Frameworks:
# Der Code basiert auf der Nutzung verschiedener Frameworks und führt zusätzliche Dateien aus.
# Einige dieser Dateien könnten automatisch weitere Abhängigkeiten installieren, die für die Funktionalität erforderlich sind.
# Es wird dringend empfohlen, die Installation und Konfiguration in einer isolierten Umgebung (z. B. einer virtuellen Umgebung) durchzuführen,
# um mögliche Konflikte mit bestehenden Softwareinstallationen zu vermeiden.
#
# Haftungsausschluss:
# Die Nutzung des Codes erfolgt vollständig auf eigene Verantwortung.
# Peharge übernimmt keinerlei Haftung für Schäden, Datenverluste, Systemfehler oder andere Probleme,
# die direkt oder indirekt durch die Nutzung, Modifikation oder Weitergabe des Codes entstehen könnten.
#
# Bitte lesen Sie die vollständigen Lizenzbedingungen der MIT-Lizenz, um sich mit Ihren Rechten und Pflichten vertraut zu machen.

from flask import Flask, render_template, request, jsonify, send_from_directory
import ollama
import os
from werkzeug.utils import secure_filename
import markdown
import re
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_URL'] = '/uploads/'
DEFAULT_IMAGE_PATH = r""

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def execute_python_code(md_content):
    """
    Searches for Python code in markdown content, executes it, and appends outputs to the markdown.
    """
    code_pattern = re.compile(r"```python(.*?)```", re.DOTALL)
    matches = code_pattern.findall(md_content)

    for match in matches:
        code = match.strip()
        try:
            # Create a new context for execution
            exec_globals = {}
            exec_locals = {}
            exec(code, exec_globals, exec_locals)

            output_text = ""
            img_html = ""

            # Check if any text output is present
            if 'output' in exec_locals:
                output_text = f"<pre>{exec_locals['output']}</pre>"

            # Check if a Matplotlib plot was generated
            fig = plt.gcf()
            if fig and fig.get_axes():
                img = io.BytesIO()
                plt.savefig(img, format='png', bbox_inches='tight')
                plt.close(fig)
                img.seek(0)
                encoded_img = base64.b64encode(img.read()).decode('utf-8')
                img_html = f'<img src="data:image/png;base64,{encoded_img}" alt="Generated Plot" />'

            # Replace the code block with executed result
            result = f"<div class='code-output-box'><pre><code>{code}</code></pre>{output_text}{img_html}</div>"
            md_content = md_content.replace(f"```python\n{code}\n```", result)

        except Exception as e:
            error_msg = f"Error executing code: {e}"
            error_html = f"<div class='code-output-box error'>Execution Error: {error_msg}</div>"
            md_content = md_content.replace(
                f"```python\n{code}\n```",
                error_html
            )
    return md_content


@app.route('/')
def index():
    return render_template('index13.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form.get('message', '').strip()
    file = request.files.get('image', None)

    if not user_message:
        return jsonify({'error': 'Message cannot be empty'}), 400

    if file and file.filename and allowed_file(file.filename):
        # Process message with uploaded image
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            response = ollama.chat(
                model='llama3.2-vision',
                messages=[{
                    'role': 'user',
                    'content': user_message,
                    'images': [filepath]
                }]
            )

            response_content = response['message']['content']
            response_content = execute_python_code(response_content)
            html_content = markdown.markdown(response_content, extensions=['extra'], output_format='html5')
            wrapped_html_content = f"<div class='response-box'>{html_content}</div>"

            return jsonify({
                'response': wrapped_html_content,
                'image_url': app.config['UPLOAD_URL'] + filename
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        # Process message without image, using the default image path
        try:
            response = ollama.chat(
                model='llama3.2-vision',
                messages=[{
                    'role': 'user',
                    'content': user_message
                }]
            )

            response_content = response['message']['content']
            response_content = execute_python_code(response_content)
            html_content = markdown.markdown(response_content, extensions=['extra'], output_format='html5')
            wrapped_html_content = f"<div class='response-box'>{html_content}</div>"

            return jsonify({
                'response': wrapped_html_content,
                'image_url': DEFAULT_IMAGE_PATH
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
