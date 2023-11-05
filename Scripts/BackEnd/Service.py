from flask import Flask, request, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename

from PPT_2_Text import process_pptx
from Notes_Process import notesprocess

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file and allowed_file(file.filename):
        result_zip_stream = process_pptx(file.stream)
        result_zip_stream.seek(0)
        filename = secure_filename('result.zip')

        return send_file(
            result_zip_stream,
            mimetype='application/zip',
            as_attachment=True,
            download_name=filename
        )

@app.route('/notes-process', methods=['POST'])
def notes_process():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file and allowed_file(file.filename):
        result_zip_stream = notesprocess(file.stream)
        result_zip_stream.seek(0)
        filename = secure_filename('notes_result.zip')

        return send_file(
            result_zip_stream,
            mimetype='application/zip',
            as_attachment=True,
            download_name=filename
        )

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'zip'

if __name__ == '__main__':
    app.run(debug=True)
