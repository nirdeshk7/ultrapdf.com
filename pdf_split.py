# pdf_split.py
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, pages, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    for page in pages:
        writer.add_page(reader.pages[page - 1])
    with open(output_pdf, 'wb') as f:
        writer.write(f)
