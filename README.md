# PDF-sandwich

A simple script for combining PDFs. 
Embeds 'inner_pdf' between front and back pages of 'outer_pdf'.
Saves combined document at 'destination_pdf'. 

Created mostly because I don't own a printer at home,
and I don't want to get told off for using shared work printer
for printing personal items (concert tickets,.. etc)

### Demo
Run the script using Python to sandwich the demo PDFs included with repo.
The demo outer_pdf pages are confusing-looking nonsense from http://thatsmathematics.com/mathgen/
The inner_pdf pages can be anything you'd like.

#### Developed using:
- Python 3.5
- PyPDF2

#### Note to self for future development goals:
- Add simple SYS ARGS for command line use
- Unit Tests?  maybe not necessary..
- Consider adding a GUI for easier use and file-picking
