from flask import Flask, render_template, request, jsonify, send_from_directory
import ollama
import os
import markdown2  # Für Markdown-zu-HTML-Konvertierung
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_URL'] = '/uploads/'

# Erstelle Upload-Ordner, falls er noch nicht existiert
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Erlaubte Dateitypen überprüfen
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index8.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form.get('message', '')
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            # Kommunikation mit dem ollama-Modell
            response = ollama.chat(
                model='llama3.2-vision',
                messages=[{
                    'role': 'user',
                    'content': user_message,
                    'images': [filepath]
                }]
            )
            response_content = response['message']['content']

            # Konvertiere das Markdown (response_content) zu HTML
            html_content = markdown2.markdown(response_content, extras=["fenced-code-blocks", "tables", "strike", "footnotes"])

            # Rückgabe der HTML-Antwort
            return jsonify({'response': html_content, 'image_url': app.config['UPLOAD_URL'] + filename})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid file type'}), 400

if __name__ == "__main__":
    app.run(debug=True)
