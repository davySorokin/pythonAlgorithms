import barcode
from io import BytesIO
from barcode import EAN13
from barcode.writer import SVGWriter

# Write to a file-like object:
rv = BytesIO()
EAN13("100000902922", writer=SVGWriter()).write(rv)