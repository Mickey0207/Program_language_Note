import requests
import re
from bs4 import BeautifulSoup

def main():
    resp = requests.get('https://www.starbucks.com.tw/home/index.jspx?r=57')
    soup = BeautifulSoup(resp.text, 'html.parser')

# 利用 regex 找出所有 .jpg 結尾的圖片
    for img in soup.find_all('img', {'src': re.compile('.jpg')}):
        print(img['src'])