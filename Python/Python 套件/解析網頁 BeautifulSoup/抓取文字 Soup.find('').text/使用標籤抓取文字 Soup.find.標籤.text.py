import requests
from bs4 import BeautifulSoup

resp = requests.get('https://jwlin.github.io/py-scraping-analysis-book/ch1/connect.html')

soup = BeautifulSoup(resp.text, 'html.parser')

get_h1 = soup.find('h1').text
# 抓取 h1 標籤的文字
print(get_h1)

get_p = soup.p.text
# 抓取 p 標籤的文字
print(get_p)

get_a = soup.p.a.text
# 抓取 p 標籤內的 a 標籤文字
print(get_a)

get_footer = soup.footer.string
# 抓取 footer 標籤的文字
print(get_footer)

main_titles = soup.find_all('h3')
# 抓取所有 h3 標籤的文字
print(main_titles)