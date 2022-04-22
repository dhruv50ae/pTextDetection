import cv2 as cv
from pytesseract import pytesseract

pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

img = cv.imread("Photos/textnum.png")

wordsInImage = pytesseract.image_to_string(img)

print(wordsInImage)
