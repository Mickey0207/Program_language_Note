str = "檔案名稱是 : "
print(str, __name__)

主檔案
在自己的檔案裡，name 會顯示為 main

引入套件時
在別的檔案裡，如引用套件，
name 會顯示成 檔案名稱

應用 防止套件自動執行

def file_name():
    
    if __name__ == '__main__':
        
        str = "檔案名稱是 : "
        print(str, __name__)

file_name()

利用檔案名稱的屬性來運用 if 迴圈，
這樣能夠有效的防止在其他檔案引用時，
讓他自動執行。

不過寫在 if 迴圈裡的內容完全無法引用。

