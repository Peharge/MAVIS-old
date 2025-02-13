# pip install "pix2tex[gui]" flask pillow

from flask import Flask, render_template, request, jsonify
from PIL import Image
from pix2tex.cli import LatexOCR
import os
import base64
import io

# Initialize Flask app
app = Flask(__name__)

# Directory to save uploaded images
UPLOAD_FOLDER_latex = 'uploads'
os.makedirs(UPLOAD_FOLDER_latex, exist_ok=True)
app.config['UPLOAD_FOLDER_latex'] = UPLOAD_FOLDER_latex

# Initialize the model
model = LatexOCR()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' in request.files:
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Save the uploaded image
        image_path_latex = os.path.join(app.config['UPLOAD_FOLDE_latex'], file.filename)
        file.save(image_path_latex)
        img_latex = Image.open(image_path_latex)

    elif 'image' in request.json:
        # Handle Base64-encoded canvas image
        image_latex_data = request.json['image']
        image_latex_data = image_latex_data.split(",")[1]  # Entferne das Präfix 'data:image/png;base64,'
        image_latex_bytes = base64.b64decode(image_latex_data)
        img_latex = Image.open(io.BytesIO(image_latex_bytes))

    else:
        return jsonify({'error': 'No image data provided'}), 400

    # Process the image and get the LaTeX prediction
    try:
        latex_code = model(img_latex)
        return jsonify({'latex': latex_code})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
