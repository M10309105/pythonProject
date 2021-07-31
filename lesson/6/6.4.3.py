#/usr/bin/python3
#
#package import
print("=" * 100)
print("6.4.3 多目錄中的套件")
print("=" * 100)

#package support __path__ , it is a list when initical

# 套件也支援一個特殊屬性 __path__。它在初始化時是一個 list，包含該套件的 __init__.py 檔案所在的目錄名稱，初始化時機是在這個檔案的程式碼被執行之前。這個變數可以被修改，但這樣做會影響將來對套件內的模組和子套件的搜尋。

# 雖然這個特色不太常被需要，但它可用於擴充套件中的模組集合。

# print(__path__)