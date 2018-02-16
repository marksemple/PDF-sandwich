#! python3
import PyPDF2


def interleavePDFs(inner_pdf_path, outer_pdf_path, destination_pdf_path):
    """ Embeds 'inner_PDF' between pages of 'outer_PDF'
        Saves a new PDF at 'destination'.

        Created mostly because I don't have a printer at home,
        and I don't want to get in trouble for using shared work printer
        for printing personal items (concert tickets,.. etc)
    """

    # get FRONTPAGE and BACKPAGE from the OUTER-PDF
    coverFile = open(outer_pdf_path, 'rb')
    coverreader = PyPDF2.PdfFileReader(coverFile)
    FrontPage = coverreader.getPage(0)
    BackPage = coverreader.getPage(coverreader.numPages - 1)

    # write Cover Page
    pdfwriter = PyPDF2.PdfFileWriter()
    pdfwriter.addPage(FrontPage)

    # get pages from INNER-PDF
    innerFile = open(inner_pdf_path, 'rb')
    innerreader = PyPDF2.PdfFileReader(innerFile)
    for pageIdx in range(innerreader.numPages):
        pageObj = innerreader.getPage(pageIdx)
        pdfwriter.addPage(pageObj)

    # write back page
    pdfwriter.addPage(BackPage)

    # Save sandwiched PDF to file
    outputFile = open(destination_pdf_path, 'wb')
    pdfwriter.write(outputFile)

    innerFile.close()
    coverFile.close()
    outputFile.close()


if __name__ == "__main__":
    # RUN ME for a demo.

    import os

    thisFolder, thisFile = os.path.split(__file__)

    outerFile = os.path.join(thisFolder, 'demo_outer_pages.pdf')
    innerFile = os.path.join(thisFolder, 'demo_inner_pages.pdf')
    destination = os.path.join(thisFolder, 'demo_combined_output.pdf')

    interleavePDFs(inner_pdf_path=innerFile,
                   outer_pdf_path=outerFile,
                   destination_pdf_path=destination)
