import os
print("Current working directory:", os.getcwd())
os.chdir(r"d:\Programming Files\VSCode_Files\Python\Lib\Project")

from PyPDF2 import PdfMerger

pdfs=["aa.pdf", "bb.pdf"]

merger= PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("cc.pdf")
merger.close()
print("Successful")
