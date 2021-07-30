#/usr/bin/python3
#
#module
print("=" * 100)
print("6.3 dir Module")
print("=" * 100)

import sys
#它列出所有類型的名稱：變數、模組、函式等。 show all variables, modules, functions...
print(dir(sys))

print("=" * 100)

#dir() 不會列出內建函式和變數的名稱。如果你想要列出它們，它們被定義在標準模組 builtins 內：
import builtins
print(dir(builtins))
