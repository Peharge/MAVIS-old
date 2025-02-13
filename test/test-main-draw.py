# pip install "pix2tex[gui]" flask pillow

from flask import Flask, render_template, request, jsonify
from PIL import Image
from pix2tex.cli import LatexOCR
import os

# Initialize Flask app
app = Flask(__name__)

# Directory to save uploaded images
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize the model
model = LatexOCR()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the uploaded image
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(image_path)

    # Process the image and get the LaTeX prediction
    try:
        img = Image.open(image_path)
        latex_code = model(img)
        return jsonify({'latex': latex_code})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
