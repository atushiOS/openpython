import requests
import pandas as pd
from bs4 import BeautifulSoup
from pprint import pprint
from time import sleep
url01 = "https://www.python.org/"
url02 = "https://tech-diary.net/python-scraping-books/"
url03 = "https://suumo.jp/chintai/tokyo/sc_shinjuku/?page={}"

# 変数d_listに空のリストを作成する
d_list = []

for i in range(1, 3):
    # 変数target_urlに、アクセス先のURLを格納する
    target_url = url03.format(i)
    res = requests.get(target_url)
    sleep(1)
    # BeautifulSoupでHTMLを解析する
    soup = BeautifulSoup(res.text, 'html5lib')
    # HTML情報をcontentsに格納
    contents = soup.find_all('div', class_='cassetteitem')
    for content in contents:
        # 変数contentからそれぞれのタグ内の特定のclassを取得して、それぞれの変数に格納
        detail = content.find('div', class_='cassetteitem_content')
        table = content.find('table', class_='cassetteitem_other')

        title = detail.find('div', class_='cassetteitem_content-title').text
        address = detail.find('li', class_='cassetteitem_detail-col1').text
        access = detail.find('li', class_='cassetteitem_detail-col2').text
        age = detail.find('li', class_='cassetteitem_detail-col3').text

        # 変数tableからすべてのtrタグを取得して、変数tr_tagsに格納
        tr_tags = table.find_all('tr', class_='js-cassette_link')
        for tr_tag in tr_tags:
            # 変数tr_tagからすべてのtdタグの3番目から6番目を、それぞれの変数に格納
            floor, price, first_fee, capacity = tr_tag.find_all('td')[2:6]
            # 変数feeとmanagement_feeに、賃料と管理費を格納する
            fee, management_fee = price.find_all('li')
            # 変数depositとgratuityに、敷金と礼金を格納する
            deposit, gratuity = first_fee.find_all('li')
            # 変数madoriとmensekiに、間取りと面積を格納する
            madori, menseki = capacity.find_all('li')
            # 変数dに、これまで取得した11項目を格納する
            d = {
                'title': title.replace('\n', '').replace('\t', ''),
                'address': address.replace('\n', '').replace('\t', ''),
                'access': access.replace('\n', '').replace('\t', ''),
                'age': age.replace('\n', '').replace('\t', ''),
                'floor': floor.text.replace('\n', '').replace('\t', ''),
                'fee': fee.text.replace('\n', '').replace('\t', ''),
                'management_fee': management_fee.text.replace('\n', '').replace('\t', ''),
                'deposit': deposit.text.replace('\n', '').replace('\t', ''),
                'gratuity': gratuity.text.replace('\n', '').replace('\t', ''),
                'madori': madori.text.replace('\n', '').replace('\t', ''),
                'menseki': menseki.text.replace('\n', '').replace('\t', '')
            }
            d_list.append(d)
# 変数d_listを使って、データフレームを作成する
df = pd.DataFrame(d_list)
# to_csv()を使って、データフレームをCSV出力する
df.to_csv('suumo_info20201111.csv', index=None, encoding='utf-8-sig')