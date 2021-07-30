#/usr/bin/python3
#
#module
import foo
import sys
print("=" * 100)
print("6.1.3 Module")
print("=" * 100)
#will create a compiled file in __pycache__ to increase effeciency
#可以在 Python 指令上使用開關參數 (switch) -O 或 -OO 來減小已編譯模組的大小。指令參數 -O 刪除 assert（斷言）陳述式，-OO 同時刪除 assert 陳述式和 __doc__ 字串。
# #由於有些程式可能依賴於上述這些內容，因此只有在您知道自己在做什麼時，才應使用此參數。「已優化」模組有 opt- 標記，且通常較小。未來的版本可能會改變優化的效果。
#讀取 .pyc 檔案時，程式的執行速度並不會比讀取 .py 檔案快。唯一比較快的地方是載入的速度。