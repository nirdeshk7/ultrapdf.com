# doc_to_pdf.py
import subprocess

def convert_to_pdf(input_path, output_path):
    subprocess.run([
        'libreoffice', '--headless', '--convert-to', 'pdf', input_path,
        '--outdir', output_path.rsplit('/', 1)[0]
    ], check=True)
