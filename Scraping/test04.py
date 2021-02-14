"""
url先から画像を取得し保存するプログラム

"""
import requests
import io
from bs4 import BeautifulSoup
from PIL import Image

url = 'https://scraping-for-beginner.herokuapp.com/image'
root_url = 'https://scraping-for-beginner.herokuapp.com'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# imgタグに書かれているHTML情報リストを取得
img_tags = soup.find_all('img')
for i, img_tag in enumerate(img_tags):
    img_url = root_url + img_tag['src']
    img = Image.open(io.BytesIO(requests.get(img_url).content))
    img.save(f'img/sample{i}.jpg')