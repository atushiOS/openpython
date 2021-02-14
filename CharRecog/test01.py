from PIL import Image
import pyocr
import cv2
import os

path_tesseract = "C:\\Program Files\\Tesseract-OCR"
if path_tesseract not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + path_tesseract

img1 = Image.open('sample01.png')
img2 = Image.open('sample02.png')

tools = pyocr.get_available_tools()
tool = tools[0]

builder = pyocr.builders.TextBuilder(tesseract_layout=6) # 0-13
txt1 = tool.image_to_string(
    img1,
    lang='jpn',
    builder=builder
)
txt2 = tool.image_to_string(
    img2,
    lang='eng+jpn',
    builder=builder
)

img_gray = cv2.imread('sample02.png', 0)
cv2.imwrite('sample03.png', img_gray)
img3 = Image.open('sample03.png')
txt3 = tool.image_to_string(
    img3,
    lang='jpn',
    builder=builder
)

results = tool.image_to_string(
    img1,
    lang='jpn',
    builder=pyocr.builders.WordBoxBuilder(tesseract_layout=11)
)

out = cv2.imread('sample01.png')
for box in results:
    cv2.rectangle(out, box.position[0], box.position[1], (0, 0, 255), 2)
cv2.imwrite('output.png', out)

