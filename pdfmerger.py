from PyPDF2 import PdfMerger
import os

merger = PdfMerger()

for items in os.listdir():
    if items.endswith('.pdf'):
        merger.append(items)

merger.write('final_merged.pdf')
merger.close()

print('PDFs merged successfully!')
