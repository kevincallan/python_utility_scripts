# split a pdf into multiple files 

from PyPDF2 import PdfFileWriter, PdfFileReader

def split_pdf(inputpdf):
    inputpdf = inputpdf
    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open("student%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)



split_pdf(inputpdf = PdfFileReader(open("/path/file.pdf", "rb")))
