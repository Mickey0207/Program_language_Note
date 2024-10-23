for iterating_var in sequence:
    statements(s)

# iterating_var     計數器當前值
# sequence          計數器值設定，預設為 1
# statements(s)     程式碼區塊

for i in range(2,9):    # 使用 range 設定計數器起始值與結束值
	print(i)

money = 100000
rate = 0.02

for i in range(1,i+1):
    money = money*(1+rate)
    print(f'第{i}年本利和是{round(money)}:')

for j in range(1,10):
    for k in range(1,10):
        print(f'{j}*{k}={j*k:2}',end = ' , ')
    print()