#/usr/bin/python3
#
#module
import foo
import sys
print("=" * 100)
print("6.1.2 Module")
print("=" * 100)

# Import 一個名為 spam 的模組時，直譯器首先會搜尋具有該名稱的內建模組。如果找不到，接下來會在變數 sys.path 所給定的資料夾清單之中，搜尋一個名為 spam.py 的檔案。sys.path 從這些位置開始進行初始化：

# 輸入腳本所位在的資料夾（如未指定檔案時，則是當前資料夾）。

# PYTHONPATH（一連串和 shell 變數 PATH 的語法相同的資料夾名稱）。

# 安裝相關的預設值。
print(sys.path)