# ultraPDF/backend/app.py
from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
from converters.pdf_merge import merge_pdfs
from converters.pdf_split import split_pdf
from converters.doc_to_pdf import convert_to_pdf

UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to ultraPDF API"})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    return jsonify({'message': 'File uploaded successfully', 'filename': filename})

@app.route('/merge', methods=['POST'])
def merge():
    files = request.json.get('files')
    output_filename = request.json.get('output', 'merged.pdf')
    output_path = os.path.join(app.config['PROCESSED_FOLDER'], output_filename)
    merge_pdfs([os.path.join(UPLOAD_FOLDER, f) for f in files], output_path)
    return send_file(output_path, as_attachment=True)

@app.route('/split', methods=['POST'])
def split():
    file = request.json.get('file')
    pages = request.json.get('pages')
    output_path = os.path.join(app.config['PROCESSED_FOLDER'], f'split_{file}')
    split_pdf(os.path.join(UPLOAD_FOLDER, file), pages, output_path)
    return send_file(output_path, as_attachment=True)

@app.route('/convert', methods=['POST'])
def convert():
    file = request.json.get('file')
    output_path = os.path.join(app.config['PROCESSED_FOLDER'], f'converted_{file}.pdf')
    convert_to_pdf(os.path.join(UPLOAD_FOLDER, file), output_path)
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# Note: You need to create converters/pdf_merge.py, pdf_split.py, doc_to_pdf.py
# I will provide these files next.
