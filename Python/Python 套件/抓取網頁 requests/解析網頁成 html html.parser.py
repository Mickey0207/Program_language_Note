import requests
from bs4 import BeautifulSoup

resp = requests.get('https://www.yannick.com.tw/shop/productlist?Item1=01&Item2=0102&Item3=010203')

soup = BeautifulSoup(resp.text, 'html.parser')
# 解析整張 Html

print(soup)