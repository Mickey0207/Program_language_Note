import requests
from bs4 import BeautifulSoup

resp = requests.get('https://www.yannick.com.tw/shop/productlist?Item1=01&Item2=0102&Item3=010203')

print(resp.status_code)
# 網頁請求測試
# 200 是成功抓取
# 404 是抓不到資料

soup = BeautifulSoup(resp.text, 'html.parser')
# 解析網頁

print(soup)
# 輸出為排版的 HTML 程式碼

print(soup.prettify())
# 輸出排版後的 HTML 程式碼