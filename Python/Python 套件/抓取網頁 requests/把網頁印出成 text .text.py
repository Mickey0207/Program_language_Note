import requests
from bs4 import BeautifulSoup

resp = requests.get('https://www.yannick.com.tw/shop/productlist?Item1=01&Item2=0102&Item3=010203')
# 請求網址

soup = BeautifulSoup(resp.text)
# 把網頁印出成 text

print(soup)