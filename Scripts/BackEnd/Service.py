from flask import Flask, request, send_file
from flask_cors import CORS
from PPT_2_Text import process_pptx
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file and allowed_file(file.filename):
        zip_path = os.path.join('uploads', 'uploaded.zip')
        file.save(zip_path)

        result_zip_path = process_pptx(zip_path)

        return send_file(result_zip_path, as_attachment=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'zip'

if __name__ == '__main__':
    app.run(debug=True)
