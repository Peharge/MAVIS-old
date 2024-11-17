from flask import Flask, render_template, request, jsonify, send_from_directory, session
import ollama
import os
from werkzeug.utils import secure_filename
import markdown
import re
import io
import sys
import base64
import matplotlib.pyplot as plt
import datetime
import numpy as np
import math
app = Flask(__name__)
# Setze einen geheimen Schlüssel für die Session
app.secret_key = os.urandom(24)  # Generiert einen zufälligen Schlüssel mit 24 Bytes
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
    Sucht nach Python-Code im Markdown-Inhalt, führt ihn aus und fügt die Ausgaben (Text oder Bild) zum Markdown hinzu.
    Falls kein Code vorhanden ist, wird "" als Ergebnis zurückgegeben.
    """
    code_pattern = re.compile(r"```python(.*?)```", re.DOTALL)
    matches = code_pattern.findall(md_content)

    # Falls kein Code gefunden wird, gib einen leeren String zurück
    if not matches:
        return "---"

    # Verzeichnis für gespeicherte Bilder
    image_dir = r"C:\Users\julia\PycharmProjects\MAVIS\static\image"
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    for match in matches:
        code = match.strip()
        try:
            # Umleiten der Ausgaben in einen String-Buffer
            old_stdout = sys.stdout
            sys.stdout = io.StringIO()
            # `plt.show()` durch Speichern ersetzen
            code = code.replace("plt.show()", "# plt.show() ersetzt durch Speichern der Grafik")
            # Kontext für die Code-Ausführung erstellen
            exec_globals = {}
            exec_locals = {}
            exec(code, exec_globals, exec_locals)
            # Erhalte alle Ausgaben, die während der Code-Ausführung erzeugt wurden
            output_text = sys.stdout.getvalue()
            # Wiederherstellen der normalen Ausgabe
            sys.stdout = old_stdout
            img_html = ""
            # Wenn eine Matplotlib-Grafik erzeugt wurde, diese als Datei speichern
            fig = plt.gcf()
            if fig and fig.get_axes():  # Überprüfen, ob eine Grafik vorhanden ist
                # Generiere einen eindeutigen Dateinamen
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                image_filename = f"fig_{timestamp}.png"
                image_path = os.path.join(image_dir, image_filename)
                # Diagramm speichern
                plt.savefig(image_path, format='png', bbox_inches='tight')
                plt.close(fig)  # Grafik schließen, um Speicher freizugeben
                # Relativer Pfad für HTML (basierend auf Flask-Static-Serving)
                image_url = f"/static/image/{image_filename}"

                # Füge das Bild in den HTML-Output ein
                img_html = f'<img class="img-out" src="{image_url}" alt="Generated Plot" />'

            # Ersetze den Codeblock im Markdown durch den Ausgabeblock (Text oder Bild)
            result = f"<div class='code-output-box'>{output_text}{img_html}</div>"

        except Exception as e:
            # Fehler beim Ausführen des Codes
            error_msg = f"Fehler beim Ausführen des Codes: {e}"
            error_html = f"<div class='code-output-box error'>Execution Error: {error_msg}</div>"
            result = error_html

        session['result'] = result
        return result

@app.route('/')
def index():
    return render_template('index13.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form.get('message', '').strip()
    result = session.get('result', '')
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
            response_content_code = execute_python_code(response_content)
            html_content = markdown.markdown(response_content, extensions=['extra'], output_format='html5')
            wrapped_html_content = f"<div class='response-box'>{html_content}</div>"

            # Hier wird das 'md_content' mit der Antwort und dem Code (als 'code') gesendet
            return jsonify({
                'response': wrapped_html_content,
                'image_url': app.config['UPLOAD_URL'] + filename,
                'code': response_content_code  # Weitergabe des Markdown-Codes
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
            response_content_code = execute_python_code(response_content)
            html_content = markdown.markdown(response_content, extensions=['extra'], output_format='html5')
            wrapped_html_content = f"<div class='response-box'>{html_content}</div>"

            return jsonify({
                'response': wrapped_html_content,
                'image_url': DEFAULT_IMAGE_PATH,
                'code': response_content_code  # Weitergabe des Markdown-Codes
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)