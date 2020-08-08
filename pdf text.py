#code for japan
pip install pdfminer.six==20200517
#
import PyPDF2
pdf_file_obj=open('meetingminutes.pdf','rd')
pdf_reader=PyPDF2.PDF2.PdfFileReader(pdf_file.obj)
pdf_reader.numPages #()
pdf_obj=pdf_reader.getpage(0) #
page_obj.extractText()


#code for japan
import camelot
Traceback (most recent call last):
File "", line 1, in
File "/usr/local/lib/python3.7/site-packages/camelot/init.py", line 6, in
from .io import read_pdf
File "/usr/local/lib/python3.7/site-packages/camelot/io.py", line 5, in
from .handlers import PDFHandler
File "/usr/local/lib/python3.7/site-packages/camelot/handlers.py", line 9, in
from .parsers import Stream, Lattice
File "/usr/local/lib/python3.7/site-packages/camelot/parsers/init.py", line 3, in
from .stream import Stream
File "/usr/local/lib/python3.7/site-packages/camelot/parsers/stream.py", line 10, in
from .base import BaseParser
File "/usr/local/lib/python3.7/site-packages/camelot/parsers/base.py", line 5, in
from ..utils import get_page_layout, get_text_objects
File "/usr/local/lib/python3.7/site-packages/camelot/utils.py", line 17, in
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
ImportError: cannot import name 'PDFTextExtractionNotAllowed' from 'pdfminer.pdfpage' (/usr/local/lib/python3.7/site-packages/pdfminer/pdfpage.py)