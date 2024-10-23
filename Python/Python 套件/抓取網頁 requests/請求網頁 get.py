import requests

resp = requests.get('https://www.yannick.com.tw/shop/productlist?Item1=01&Item2=0102&Item3=010203')
# 請求網頁

print(resp)
# 回傳是否抓取到網頁
# 200 代表成功
# 404 代表無資料