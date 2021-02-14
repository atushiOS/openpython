"""
url先から値を取得しターミナル上に表示するプログラム

"""
import requests
from bs4 import BeautifulSoup

url = 'https://scraping-for-beginner.herokuapp.com/udemy'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# pタグ(class:subscribers)に書かれている受講生の数を表示
subscribers = soup.find_all('p', attrs={'class': 'subscribers'})[0]
n_subscribers = int(subscribers.text.split('：')[1])
print(n_subscribers)

# pタグ(class:reviews)に書かれているレビューの数を表示
reviews = soup.find_all('p', attrs={'class': 'reviews'})[0]
n_reviews = int(reviews.text.split('：')[1])
print(n_reviews)

# classタグ検索はこの表記でも可能
print(soup.select_one('.subscribers'))