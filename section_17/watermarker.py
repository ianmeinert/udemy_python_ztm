from os import path
from PyPDF2 import PdfReader, PdfWriter


def watermark(content_pdf, stamp_pdf, pdf_result):
    reader = PdfReader(content_pdf)
    writer = PdfWriter()
    # watermark all the pages
    page_indices = list(range(0, len(reader.pages)))

    for i in page_indices:
        content_page = reader.pages[i]
        mediabox = content_page.mediaBox

        reader_stamp = PdfReader(stamp_pdf)
        image_page = reader_stamp.pages[0]

        image_page.merge_page(content_page)
        image_page.mediabox = mediabox
        writer.add_page(image_page)

    with open(pdf_result, "wb") as fp:
        writer.write(fp)


pdf_path = 'Pdfs'
stamp_pdf = path.join(pdf_path, 'wtr.pdf')
pdf_result = path.join(pdf_path, 'watermarked.pdf')
content_pdf = path.join(pdf_path, 'supermerged.pdf')

watermark(content_pdf, stamp_pdf, pdf_result)
