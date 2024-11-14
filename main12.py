from flask import Flask, render_template, request, jsonify, send_from_directory
import ollama
import os
from werkzeug.utils import secure_filename
import markdown

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_URL'] = '/uploads/'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def allowed_file(filename):
    """Überprüft, ob die Datei einen erlaubten Bildtyp hat"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Lädt die Hauptseite"""
    return render_template('index11.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Gibt hochgeladene Bilder zurück"""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/send_message', methods=['POST'])
def send_message():
    """Verarbeitet Text und optional ein Bild und schickt es an das Modell"""
    user_message = request.form.get('message', '').strip()

    if not user_message:
        return jsonify({'error': 'Nachricht darf nicht leer sein.'}), 400

    file = request.files.get('image')
    image_path = None

    if file and file.filename != '' and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(image_path)

    try:

        messages = [{
            'role': 'user',
            'content': user_message
        }]


        if image_path:
            messages[0]['images'] = [image_path]

        response = ollama.chat(
            model='llama3.2-vision',
            messages=messages
        )

        response_content = response['message']['content']
        html_content = markdown.markdown(response_content, extensions=['extra'], output_format='html5')
        wrapped_html_content = f"<div style='display:block;'>{html_content}</div>"

        response_data = {'response': wrapped_html_content}

        if image_path:
            response_data['image_url'] = app.config['UPLOAD_URL'] + filename

        return jsonify(response_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
