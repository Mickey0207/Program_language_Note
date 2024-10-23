import matplotlib.pyplot as plt
import numpy as np
# make data
a = []                      #月份資料集合
b = []                      #每月支出資料集合
for i in range(1,7):        #產出六個月的資料
    a.append(i)             #輸入月份資料
    b.append(2**i)          #輸入每月支出資料
print('a = ' ,a,'b = ',b)   #列印資料

# plot
fig, ax = plt.subplots()

ax.plot(a, b, 'x')
# 圖表類型更換看以下 替換 plot 即可更換

plt.show()
