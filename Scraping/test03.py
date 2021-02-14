"""
url先からランキングの各値を取得しcsv形式に保存するプログラム

"""
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://scraping-for-beginner.herokuapp.com/ranking/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# ## 1つの観光地情報を取得
# spots = soup.find_all('div', attrs={'class': 'u_areaListRankingBox'})
# spot = spots[0]

# # 観光地名
# spot_name = spot.find('div', attrs={'class': 'u_title'})
# spot_name.find('span', attrs={'class': 'badge'}).extract()
# spot_name = spot_name.text.replace('\n', '')
# # 評点
# eval_num = spot.find('div', attrs={'class': 'u_rankBox'})
# eval_num = float(eval_num.text.replace('\n', ''))
# # 各スコア
# categoryItems = spot.find('div', attrs={'class': 'u_categoryTipsItem'})
# categoryItems = categoryItems.find_all('dl')

# details = {}
# for categoryItem in categoryItems:
#     category = categoryItem.dt.text
#     rank = float(categoryItem.span.text)
#     details[category] = rank

# datum = details
# datum['観光地名'] = spot_name
# datum['評点'] = eval_num

data = []
spots = soup.find_all('div', attrs={'class': 'u_areaListRankingBox'})
for spot in spots:
    # divタグ(class:u_title)に書かれている観光地名を取得
    spot_name = spot.find('div', attrs={'class': 'u_title'})
    spot_name.find('span', attrs={'class': 'badge'}).extract()
    spot_name = spot_name.text.replace('\n', '')
    # divタグ(class:u_rankBox)に書かれている評点を取得
    eval_num = spot.find('div', attrs={'class': 'u_rankBox'})
    eval_num = float(eval_num.text.replace('\n', ''))
    # divタグ(class:u_categoryTipsItem)に書かれているスコアリストを取得
    categoryItems = spot.find('div', attrs={'class': 'u_categoryTipsItem'})
    categoryItems = categoryItems.find_all('dl')
    # datamに格納
    datum = {}
    for categoryItem in categoryItems:
        category = categoryItem.dt.text
        rank = float(categoryItem.span.text)
        datum[category] = rank
    datum['観光地名'] = spot_name
    datum['評点'] = eval_num
    data.append(datum)

df = pd.DataFrame(data)
# カラム順入れ替え
df = df[['観光地名', '評点', '楽しさ', '人混みの多さ', '景色', 'アクセス']]
# csv出力（indexなし、UTF-8）
df.to_csv('観光地情報.csv', index=None, encoding='utf-8-sig')