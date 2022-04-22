import cv2 as cv
from pytesseract import pytesseract
from pytesseract import Output

pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

img = cv.imread("Photos/textnum.png")

imageData = pytesseract.image_to_data(img, output_type=Output.DICT)

for i, word in enumerate(imageData['text']):
    if word != "":
        x, y, w, h = imageData["left"][i], imageData["top"][i], imageData["width"][i], imageData["height"][i],
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        cv.putText(img, word, (x, y-16),
                   cv.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 1)

cv.imshow("Window", img)
cv.waitKey(0)
