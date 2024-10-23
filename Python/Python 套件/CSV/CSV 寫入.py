import csv
path = 'C:/Users/walke/Desktop/data_file.csv' # 建立路徑
with open(path,'w',newline='') as data_file:
    # path          打開 CSV 路徑
    # 'W'           寫入模式
    # data_file     打開的 CSV 檔案名稱
    
    writer = csv.writer(data_file)  # 設定 CSV 變數名稱

    #Write data
    writer.writerow(['姓名','身高','體重'])
    writer.writerow(['又成','180','80'])
    writer.writerow(['結語','170','70'])
print("寫入完成")