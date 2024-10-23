import csv
path = 'C:/Users/walke/Desktop/Data.csv'# 建立路徑
with open(path,'r',encoding='utf8') as data_file:
    # path          打開 CSV 路徑
    # 'r'           讀取模式
    # data_file     打開的 CSV 檔案名稱
    
    read = csv.reader(data_file)   # 設定 CSV 變數名稱

    #Read data
    for r in read:
        print(r)

print("讀取完成")