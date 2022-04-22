import cv2 as cv
from pytesseract import pytesseract

pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

img = cv.imread("Photos/textnum.png")
height, width, c = img.shape

letterBoxes = pytesseract.image_to_boxes(img)

for box in letterBoxes.splitlines():
    box = box.split()
    print(box)
    x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv.rectangle(img, (x, height-y), (w, height-h), (0, 0, 255), 3)
    cv.putText(img, box[0], (x, height-h+32),
    cv.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 1)

cv.imshow("Window", img)
cv.waitKey(0)
