import requests
import pandas as pd
import chromedriver_binary
from bs4 import BeautifulSoup
from pprint import pprint
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
url = "https://www.jucda.or.jp/tekisei-hanbaiten/shops.php?pref_cd={}&page={}"
url01 = "https://test.ohanasiya.net/zipper/"

# 変数d_listに空のリストを作成する
d_list = []
shop_list = []
address_list = []
tel_list = []

for i in range(1, 48):
    for j in range(1, 100):
        # 変数target_urlに、アクセス先のURLを格納する
        target_url = url.format(i, j)
        res = requests.get(target_url)
        sleep(1)
        # BeautifulSoupでHTMLを解析する
        soup = BeautifulSoup(res.text, 'html5lib')
        # HTML情報をcontentsに格納
        contents = soup.find_all('dl', class_='search-result')
        if len(contents) == 0:
            break
        for content in contents:
            # 変数contentからそれぞれのタグ内の特定のclassを取得して、それぞれの変数に格納
            shop = content.find('p', class_='shop-title').text
            address = content.find('p', class_='address').text
            tel = content.find('p', class_='tel').text
            d = {
                'shop': shop.replace('\u3000', ' '),
                'address': address,
                'tel': tel.replace('TEL: ','') 
            }
            d_list.append(d)
        print('finished {}, {}'.format(i, j))

df = pd.DataFrame(d_list)
df.to_csv('image_urls.csv', index=None, encoding='utf-8-sig')

# # --> STEP1 : Yahoo画像検索に自動でアクセスする
# options = webdriver.ChromeOptions()
# options.add_argument('--incognito')

# driver = webdriver.Chrome(options=options)
# driver.get(url01)

# sleep(10)

# # --> STEP2 : プログラミングで検索する
# query = address_list[0]
# for i in range(1, len(address_list)):
#     query += '\n' + address_list[i]
# search_box = driver.find_element_by_class_name('datatextarea')
# search_box.send_keys(query)
# button = driver.find_element_by_tag_name('input')
# button.click()

# sleep(10)
# # --> STEP4 : 画像のURLを取得して、データフレームの形で保存しておく
# elements = driver.find_elements_by_id('out')
# # elements.get_attribute('value')

# print(elements)