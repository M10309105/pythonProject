#!/usr/bin/python3
#https://docs.python.org/zh-tw/3/tutorial/controlflow.html
# if 陳述式

x = int(input("Please input a integer: "))
if x < 0:
    print("%d is < 0" % x)
elif x > 0:
    print("%d is > 0" % x)
else:
    print("%d is = 0" % x)



