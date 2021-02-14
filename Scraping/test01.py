from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import chromedriver_binary
import pandas as pd

options = Options()
options.add_argument('--headless')

browser = webdriver.Chrome(options=options)
url = 'https://scraping-for-beginner.herokuapp.com/login_page'
browser.get(url)

# username, password, buttonの要素の位置を取得
elem_username = browser.find_element_by_id('username')
elem_password = browser.find_element_by_id('password')
elem_login_btn = browser.find_element_by_id('login-btn')

# username, password, buttonの要素に値を入力
elem_username.send_keys('imanishi')
elem_password.send_keys('kohei')
sleep(1)
elem_login_btn.click()

# 各id名から値を取得
name = browser.find_element_by_id('name')
company = browser.find_element_by_id('company')
birthday = browser.find_element_by_id('birthday')
come_from = browser.find_element_by_id('come_from')
hobby = browser.find_element_by_id('hobby')

print("{}\n{}\n{}\n{}\n{}".format(name.text, company.text, birthday.text, come_from.text, hobby.text.replace('\n', ',')))

# それぞれのタグからの値リストを取得
elems_th = browser.find_elements_by_tag_name('th')
elems_td = browser.find_elements_by_tag_name('td')

keys = []
for elem_th in elems_th:
    key = elem_th.text
    keys.append(key)

values = []
for elem_td in elems_td:
    value = elem_td.text
    values.append(value)

# 辞書形式に格納
df  = pd.DataFrame()
df['項目'] = keys
df['値'] = values

df.to_csv('講師情報.csv', index=None, encoding='utf-8-sig')

sleep(3)
browser.quit()