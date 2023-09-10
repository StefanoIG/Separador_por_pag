from PyPDF2 import PdfReader, PdfWriter

pdf_reader = PdfReader("pdf_unido.pdf")
                       #Aqui se pone el pdf)

for index, page in enumerate(pdf_reader.pages):
    #Indexea las paginas
    pdf_writer=PdfWriter()
    #va leyendo y separando las paginas
    pdf_writer.add_page(page)
    with open(f"page_{index + 1}.pdf", "wb") as out:
        #proceso de salida de pagina en pdf
        pdf_writer.write(out)
