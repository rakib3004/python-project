import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open("Scrum4.png") # the second one
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp2.png')
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
print('ok')
text = pytesseract.image_to_string(Image.open('Scrum4.png'), lang="ben")
print('ok')
print(text)