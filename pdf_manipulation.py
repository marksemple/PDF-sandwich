# pdf_manipulation.py

import PyPDF2

def interleavePDFs(coverPDFpath, internalPDFpath, outputPDFpath):
    """ Puts all of internalPDF inbetween first and last pages of coverPDF
        Saves new PDF at outputPath """

    pdfwriter = PyPDF2.PdfFileWriter()

    # get FRONTPAGE and BACKPAGE from the cover pdf
    coverFile = open(coverPDFpath, 'rb')
    innerFile = open(internalPDFpath, 'rb')

    coverreader = PyPDF2.PdfFileReader(coverFile)
    FrontPage = coverreader.getPage(0)
    BackPage = coverreader.getPage(coverreader.numPages - 1)

    pdfwriter.addPage(FrontPage)

    innerreader = PyPDF2.PdfFileReader(innerFile)
    for pageIdx in range(innerreader.numPages):
        pageObj = innerreader.getPage(pageIdx)
        pdfwriter.addPage(pageObj)

    pdfwriter.addPage(BackPage)

    outputFile = open(outputPDFpath, 'wb')
    pdfwriter.write(outputFile)

    coverFile.close()
    innerFile.close()
    outputFile.close()


if __name__ == "__main__":

    import os

    head, tail = os.path.split(__file__)


    coverFile = os.path.join(head, 'external_pages.pdf')
    innerFile = os.path.join(head, 'internal_pages.pdf')
    destination = os.path.join(head, 'combinedPDF.pdf')

    interleavePDFs(coverFile, innerFile, destination)


