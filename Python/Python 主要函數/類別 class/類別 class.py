class Personal():       # 建立一個類別是 Personal
    def __init__(self, name = 'name', id = 'id', fee = 'fee'):
        # _init_    預設屬性，有類別後要建立資料夾，這就是預設資料夾
        # self      一定要打，就像資料夾內要取用的檔案
        # name      檔案裡要放的元素就是寫在這
        # 'name'    元素預設賦值，可打可不打
        self.name = name
        self.id = id
        self.fee = fee
        
    def info(self):         # 新增一個資料夾，複製 self 檔案過來用
        print(f'會員編號 : {self.id}')
            
    def get_discount(self): # 新增一個資料夾，複製 self 檔案過來用
        print(f'的費用是 : {self.fee} 元')

class member(Personal):    # 將 Personal 複製過來，無須再建立 __init__
    def member(self):    
        super().info()     # 利用 super() 複製 Personal 的 info()
        print("您是一般會員")
    def get_discount(self):
        money = self.fee * 0.8
        print(f'的費用是 : {self.fee} 元，打折後為 : {money}')


member1 = Personal('lee', '10052', 15000)
# 在 Personal 裡面新增一筆 member1 的資料
member1.info()
# 利用建立好的 info 函式印出資料

member2 = member('lee', '100', 150)
# 利用複製的 Personal 新增一筆資料
member2.member()
# 利用建立好的 member() 函式印出資料