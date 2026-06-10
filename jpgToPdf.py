from PIL import Image

# Open the JPG image
image = Image.open(r"D:\Programming Files\VSCode_Files\khalid.jpg")

# Convert image to RGB
rgb_image = image.convert("RGB")

# Save as PDF
rgb_image.save(r"D:\Programming Files\VSCode_Files\Khalid.pdf")

print("JPG converted to PDF successfully!")