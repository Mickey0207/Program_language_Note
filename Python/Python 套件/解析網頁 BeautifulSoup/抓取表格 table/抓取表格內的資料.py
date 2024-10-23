import requests
from bs4 import BeautifulSoup

def main():
    resp = requests.get('http://blog.castman.net/py-scraping-analysis-book/ch2/table/table.html')
    soup = BeautifulSoup(resp.text, 'html.parser')

    prices = []
    # 建立資料陣列
    rowsa = soup.find('table', 'table')
    # 找到 (table標籤, table 標籤中的 table 屬性)
    rowsb = rowsa.tbody.find_all('tr')
    # 先找到 table 中的 tr 標籤

    #print(rowsb);
    for row in rowsb:
        price = row.find_all('td')[2].text
        # 尋找表格中的第二欄 [2]，然後用文字樣式
        print(price)
        prices.append(int(price))
        # 將找到的東西放入 price 串列裡面
        
    print(prices)
    print(sum(prices)/len(prices))#平均

if __name__ == '__main__':
    main()