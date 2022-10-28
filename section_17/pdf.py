import PyPDF2
from os import path

pdf_file = 'dummy.pdf'
pdf_folder = 'Pdfs'
new_pdf_file = 'tilt.pdf'

file_path = path.join(pdf_folder, pdf_file)
with open(file_path, 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)

    page = reader.getPage(0)
    page.rotateCounterClockwise(90)

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    tilt_path = path.join(pdf_folder, new_pdf_file)
    with open(tilt_path, 'wb') as new_file:
        writer.write(new_file)
