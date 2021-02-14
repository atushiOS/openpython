from PIL import Image
import streamlit as st
import pyocr
import cv2
import os

# path_tesseract = "C:\\Program Files\\Tesseract-OCR"
# if path_tesseract not in os.environ["PATH"].split(os.pathsep):
#     os.environ["PATH"] += os.pathsep + path_tesseract

st.title('文字認識アプリ')

SUBSCRIPTION_KEY = 'c84e2ba318844114a092bab1eda8509b'
assert SUBSCRIPTION_KEY

face_api_url = 'https://20210212ishida.cognitiveservices.azure.com/face/v1.0/detect'

uploaded_file = st.file_uploader("Choose an image...",)
if uploaded_file is not None:
    img = Image.open(uploaded_file)

    tools = pyocr.get_available_tools()
    tool = tools[0]

    builder = pyocr.builders.TextBuilder(tesseract_layout=1) # 0-13
    txt = tool.image_to_string(
        img,
        lang='jpn',
        builder=builder
    )
    txt1 = txt.replace('\n',' ').replace(' ','')
    st.write(txt1)

    builder = pyocr.builders.TextBuilder(tesseract_layout=3) # 0-13
    txt = tool.image_to_string(
        img,
        lang='jpn',
        builder=builder
    )
    txt1 = txt.replace('\n',' ').replace(' ','')
    st.write(txt1)

    builder = pyocr.builders.TextBuilder(tesseract_layout=4) # 0-13
    txt = tool.image_to_string(
        img,
        lang='jpn',
        builder=builder
    )
    txt1 = txt.replace('\n',' ').replace(' ','')
    st.write(txt1)

    builder = pyocr.builders.TextBuilder(tesseract_layout=5) # 0-13
    txt = tool.image_to_string(
        img,
        lang='jpn',
        builder=builder
    )
    txt1 = txt.replace('\n',' ').replace(' ','')
    st.write(txt1)

    builder = pyocr.builders.TextBuilder(tesseract_layout=6) # 0-13
    txt = tool.image_to_string(
        img,
        lang='jpn',
        builder=builder
    )
    txt1 = txt.replace('\n',' ').replace(' ','')
    st.write(txt1)

    builder = pyocr.builders.TextBuilder(tesseract_layout=7) # 0-13
    txt = tool.image_to_string(
        img,
        lang='jpn',
        builder=builder
    )
    txt1 = txt.replace('\n',' ').replace(' ','')
    st.write(txt1)

    builder = pyocr.builders.TextBuilder(tesseract_layout=8) # 0-13
    txt = tool.image_to_string(
        img,
        lang='jpn',
        builder=builder
    )
    txt1 = txt.replace('\n',' ').replace(' ','')
    st.write(txt1)

    builder = pyocr.builders.TextBuilder(tesseract_layout=9) # 0-13
    txt = tool.image_to_string(
        img,
        lang='jpn',
        builder=builder
    )
    txt1 = txt.replace('\n',' ').replace(' ','')
    st.write(txt1)

    builder = pyocr.builders.TextBuilder(tesseract_layout=10) # 0-13
    txt = tool.image_to_string(
        img,
        lang='jpn',
        builder=builder
    )
    txt1 = txt.replace('\n',' ').replace(' ','')
    st.write(txt1)

    builder = pyocr.builders.TextBuilder(tesseract_layout=11) # 0-13
    txt = tool.image_to_string(
        img,
        lang='jpn',
        builder=builder
    )
    txt1 = txt.replace('\n',' ').replace(' ','')
    st.write(txt1)

    builder = pyocr.builders.TextBuilder(tesseract_layout=12) # 0-13
    txt = tool.image_to_string(
        img,
        lang='jpn',
        builder=builder
    )
    txt1 = txt.replace('\n',' ').replace(' ','')
    st.write(txt1)

    builder = pyocr.builders.TextBuilder(tesseract_layout=13) # 0-13
    txt = tool.image_to_string(
        img,
        lang='jpn',
        builder=builder
    )
    txt1 = txt.replace('\n',' ').replace(' ','')
    st.write(txt1)