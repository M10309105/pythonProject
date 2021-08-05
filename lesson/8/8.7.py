#/usr/bin/python3
#
#Exception

print("=" * 100)
print("8.7 clean action")
print("=" * 100)

try:
    a = 1 / 0
except Exception as e:
    print(e)
finally:
    print("=" * 100)
    print("last version in try no matter the exception be raised")
    print("=" * 100)

#but there has some conditions...
"""
若一個例外發生於 try 子句的執行過程，則該例外會被某個 except 子句處理。如果該例外沒有被 except 子句處理，它會在 finally 子句執行後被重新引發。

一個例外可能發生於 except 或 else 子句的執行過程。同樣地，該例外會在 finally 子句執行後被重新引發。

如果 finally 子句執行 break、continue 或 return 陳述式，則例外不會被重新引發。

如果 try 陳述式遇到 break、continue 或 return 陳述式，則 finally 子句會在執行 break、continue 或 return 陳述式之前先執行。

如果 finally 子句中包含 return 陳述式，則回傳值會是來自 finally 子句的 return 陳述式的回傳值，而不是來自 try 子句的 return 陳述式的回傳值。
"""
def foo():
    try:
        return True
    finally:
        return False

#False
foo()

print("=" * 100)
def foo1(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division zero")
    else:
        print("result:",result)
    finally:
        print("finally.")

print("-" * 100)
foo1(2,1)
print("-" * 100)
foo1(2,0)
print("-" * 100)
#no one handle the exception so that raise error after finally
foo1("2","1")

#在真實應用程式中，finally 子句對於釋放外部資源（例如檔案或網路連線）很有用，無論該資源的使用是否成功。
