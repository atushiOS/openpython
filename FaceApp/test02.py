import streamlit as st
import io
import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

st.title('顔認識アプリ')

SUBSCRIPTION_KEY = 'c84e2ba318844114a092bab1eda8509b'
assert SUBSCRIPTION_KEY

face_api_url = 'https://20210212ishida.cognitiveservices.azure.com/face/v1.0/detect'

uploaded_file = st.file_uploader("Choose an image...", type='jpg')
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    with io.BytesIO() as output:
        img.save(output, format="JPEG")
        binary_img = output.getvalue()
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}
    params = {
        'returnFaceId': 'true',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
    }
    res = requests.post(face_api_url, params=params, headers=headers, data=binary_img)

    results = res.json()
    for result in results:
        rect = result['faceRectangle']
        gender = result['faceAttributes']['gender']
        age = result['faceAttributes']['age']
        text = gender + ', ' + str(age)

        font = ImageFont.truetype("arial.ttf", 15)
        size = font.getsize(text)

        draw = ImageDraw.Draw(img)
        draw.rectangle([(rect['left'], rect['top']), (rect['left']+rect['width'], rect['top']+rect['height'])], fill=None, outline='green', width=2)
        draw.text((rect['left'], rect['top'] - size[1]), text, font=font, fill='green')

    st.image(img, caption='Uploaded Image.', use_column_width=True)