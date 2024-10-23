fruits = {'apple':90,'orange':55,'banana':60}   # 字典建立
# '查詢值':賦值

a = []
for i,j in tra_dict.items():    #字典轉串列
    #print(i,j,end=',')
    a.append(i)
    a.append(j)
print(a)
print(type(a))