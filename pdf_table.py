# pip install camelot-py

import camelot as cl
table = cl.read_pdf('table.pdf', pages='all')
print(table)
