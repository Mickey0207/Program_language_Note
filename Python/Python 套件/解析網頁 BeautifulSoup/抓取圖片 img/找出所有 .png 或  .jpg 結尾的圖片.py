import requests
import re
from bs4 import BeautifulSoup

def main():
    resp = requests.get('https://www.starbucks.com.tw/home/index.jspx?r=57')
    soup = BeautifulSoup(resp.text, 'html.parser')

# 找出所有 .png 結尾的圖片
    imgs = soup.find_all('img')
    for img in imgs:
        if 'src' in img.attrs:
            if img['src'].endswith('.png'):
                print(img['src'])



找出所有 .png 結尾且含 'banner_pc_06.jpg' 的圖片



import requests
import re
from bs4 import BeautifulSoup

def main():
    resp = requests.get('https://www.starbucks.com.tw/home/index.jspx?r=57')
    soup = BeautifulSoup(resp.text, 'html.parser')

# 找出所有 .png 結尾且含 'banner_pc_06.jpg' 的圖片
    imgs = soup.find_all('img')
    for img in imgs:
        if 'src' in img.attrs:
            if 'h2-pic-02.png' in img['src'] and img['src'].endswith('.png'):
                print(img['src'])
    
# 利用 regex 找出所有 .jgp 結尾且含 'banner_pc_06.jpg' 的圖片
    for img in soup.find_all('img', {'src': re.compile('banner_pc_06.jpg')}):
        print(img['src'])