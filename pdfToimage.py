import os
from pdf2image import convert_from_path

pdf_file = r"D:\Programming Files\VSCode_Files\FIFA.pdf"
poppler_bin = r"D:\Programming Files\VSCode_Files\Python\poppler-25.12.0\Library\bin"

print(f"Checking PDF: {os.path.exists(pdf_file)}")
print(f"Checking Poppler Path: {os.path.exists(poppler_bin)}")

if os.path.exists(poppler_bin):
    print(f"Checking for pdftoppm.exe: {os.path.exists(os.path.join(poppler_bin, 'pdftoppm.exe'))}")

try:
    pages = convert_from_path(pdf_file, poppler_path=poppler_bin)
    pages[0].save("FIFA.jpg", "JPEG")
    print("Success!")
except Exception as e:
    print(f"\nSTILL FAILING: {e}")











    