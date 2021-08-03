#/usr/bin/python3
#
#Exception handle
print("=" * 100)
print("8.2 Exceptionr")
print("=" * 100)

#由使用者產生的程式中斷會引發 KeyboardInterrupt 例外信號。
while True:
    try:
        x = int(input("please input a number："))
        break
    #can use multiple error but only one will be process
    # except (RuntimeError, TypeError, NameError):
    except ValueError:
        print("not number")


#exception class

class A(Exception):
    pass

class B(A):
    pass

class C(B):
    pass

for cls in [A,B,C]:
    try:
        raise cls()
    except C:
        print("This is C")
    except B:
        print("This is B")
    except A:
        print("This is A")

#exception will print first match 
#it print AAA if except sequence is A B C like
#  try:
#         raise cls()
#     except A:
#         print("This is A")
#     except B:
#         print("This is B")
#     except C:
#         print("This is C")

#the last except can omit but carfule
import sys

try:
    f = open('lesson/7/test.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
else:
    print("This is last code had execute")


try:
    raise Exception('spam', 'eggs')
except Exception as e:
    print(type(e))    # the exception instance
    print(e.args)     # arguments stored in .args
    print(e)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = e.args     # unpack args
    print('x =', x)
    print('y =', y)
else:
    print("This is last code had execute")

#則它們會被印在未處理例外的訊息的最後一部分（「細節」）
try:
    a = 1/0
except Exception as e:
    print("error:",e)
