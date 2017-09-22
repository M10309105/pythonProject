""" input the number and compare with zero """

"""
str.isnumeric()  ==>check str whether all element are number , if navigate is false
int(xxx)		==>change type to int
float(xxx)		===>change to float

check type mether
import types 
type(x) is types.IntType 
type(x) is types.StringType  

switch 
score = int(input('請輸入分數：'))
level = score // 10
{
    10 : lambda: print('Perfect'),
    9  : lambda: print('A'),
    8  : lambda: print('B'),
    7  : lambda: print('C'),
    6  : lambda: print('D')
}.get(level, lambda: print('E'))()

check type
isinstance(input , classinfo)
classinfo:  int, str, float, list
"""
import types

while 1:
	x = input("please input a number ")
	#print("input type is " + str(type(x)))
	
	try:
		x=int(x)
		print(type(x))
	except:
		print("please input integer ")
		continue
		
		
	if x < 0 :
		print("your input number "+str(x)+" is under zero")
	elif x == 0:
		print("your input number "+str(x)+" is zero")
	elif x > 0:
		print("your input number "+str(x)+" is bigger zero")

		