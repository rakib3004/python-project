from PIL import Image
import pytesseract as tess

print(tess.image_to_string(Image.open('Scrum4.png'), lang='ben'))