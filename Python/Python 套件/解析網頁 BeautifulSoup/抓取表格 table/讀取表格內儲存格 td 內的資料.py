import requests

from bs4 import BeautifulSoup


def main():

    esp = requests.get('http://jwlin.github.io/py-scraping-analysis-book/ch2/table/table.html')
    soup = BeautifulSoup(resp.text, 'html.parser')
    rows = soup.find('table', 'table').tbody.find_all('tr')

    # 為了告訴下面 for 迴圈的範圍，所以需要上面這行
    # 用 soup 找到 table 標籤，的 table 屬性
    # 再找到所有的 tr 標籤

    for row in rows:
        all_tds = row.find_all('td')
        # 找到所有的 td 標籤

        if 'href' in all_tds[3].a.attrs:
            href = all_tds[3].a['href']     # 如果找到 href 那就 把 href 換成網址
        else:
            href = None

        print(all_tds[0].text, all_tds[1].text, all_tds[2].text, href, all_tds[3].a.img['src'])

if __name__ == '__main__':

    main()