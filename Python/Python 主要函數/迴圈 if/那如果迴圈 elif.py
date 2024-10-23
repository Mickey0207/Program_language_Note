num = 30
num = int(input("請問您的評價?"))
print(str((num))+ ("分"))
if num > 90:
    print("分數是" + str((num)) + "分")
    print("超好吃")
elif num > 60:
    print("分數是" + str((num)) + "分")
    print("不好吃")      
else:
    print("分數是" + str((num)) + "分")
    print("難吃")
