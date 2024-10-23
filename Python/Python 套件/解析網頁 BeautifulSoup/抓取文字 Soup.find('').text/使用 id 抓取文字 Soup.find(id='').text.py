import requests
from bs4 import BeautifulSoup

resp = requests.get('https://jwlin.github.io/py-scraping-analysis-book/ch1/connect.html')
soup = BeautifulSoup(resp.text, 'html.parser')

get_h1 = soup.find(id='mac-p').text
# 使用 id 抓取文字
print(get_h1)

get_h2 = soup.find('a', {'data-foo': 'mac-foo'}).text
# id 有特殊字元時，需要用字典方式尋找 id 標籤
print(get_h2)