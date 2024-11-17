from flask import Flask, render_template, request, jsonify, send_from_directory
import ollama
import os
from werkzeug.utils import secure_filename
import markdown
import re
import io
import sys
import base64
import matplotlib.pyplot as plt
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_URL'] = '/uploads/'
DEFAULT_IMAGE_PATH = r"C:\Users\julia\OneDrive - Gewerbeschule Lörrach\Pictures\3ds max.png"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def execute_python_code(md_content):
    """
    Sucht nach Python-Code im Markdown-Inhalt, führt ihn aus und fügt die Ausgaben (Text oder Bild) zum Markdown hinzu.
    """
    code_pattern = re.compile(r"```python(.*?)```", re.DOTALL)
    matches = code_pattern.findall(md_content)

    for match in matches:
        code = match.strip()
        try:
            # Umleiten der Ausgaben in einen String-Buffer
            old_stdout = sys.stdout
            sys.stdout = io.StringIO()

            # Kontext für die Code-Ausführung erstellen
            exec_globals = {}
            exec_locals = {}
            exec(code, exec_globals, exec_locals)

            # Erhalte alle Ausgaben, die während der Code-Ausführung erzeugt wurden
            output_text = sys.stdout.getvalue()

            # Wiederherstellen der normalen Ausgabe
            sys.stdout = old_stdout

            img_html = ""

            # Wenn eine Matplotlib-Grafik erzeugt wurde, diese als Bild einfügen
            fig = plt.gcf()
            if fig and fig.get_axes():  # Überprüfen, ob eine Grafik vorhanden ist
                img = io.BytesIO()
                plt.savefig(img, format='png', bbox_inches='tight')
                plt.close(fig)  # Grafik schließen, um Speicher freizugeben
                img.seek(0)
                encoded_img = base64.b64encode(img.read()).decode('utf-8')
                img_html = f'<img src="data:image/png;base64,{encoded_img}" alt="Generated Plot" />'

            # Ersetze den Codeblock im Markdown durch den Ausgabeblock (Text oder Bild)
            result = f"<div class='code-output-box'><pre><code>{code}</code></pre>{output_text}{img_html}</div>"
            md_content = md_content.replace(f"```python\n{code}\n```", result)

        except Exception as e:
            error_msg = f"Fehler beim Ausführen des Codes: {e}"
            error_html = f"<div class='code-output-box error'>Execution Error: {error_msg}</div>"
            md_content = md_content.replace(f"```python\n{code}\n```", error_html)
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
        # Verarbeite die Nachricht mit dem hochgeladenen Bild
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
        # Verarbeite die Nachricht ohne Bild, benutze das Standardbild
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
