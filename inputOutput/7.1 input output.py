#7-1 input and output
#https://docs.python.org.tw/3/tutorial/inputoutput.html

#string formatting functions: str() and repr()

#Both str and repr can generate representation string , str for human readable; repr can generate interpreter string

ss="Hello, world"
print(str(ss))  #"Hello, world"

print(str(1/7)) #'0.14285714285714285'

Y = "hello, world\nasd" #

print(Y) 
"""
hello, world
asd
"""
print(str(Y))
"""
hello, world
asd
"""
print(repr(Y))   #'hello, world\nasd'

#Write table  
"""
str.rjust() can add space which right justifies  string. If want left or center can use ljust() center()
"""
for x in range(1,11):
	print(repr(x).rjust(2),repr(x*x).ljust(3),repr(x*x*x).center(4)[:4])

#other way
"""
{keynumber:value} .format(key0,key1,key2)
"""
for x in range(1,11):
	print("{0:2d} {1:3d} {2:4d}".format(x,x*x,x*x*x))

# str.zfill() can add zero to numeric variable
print("5".zfill(5))

#str.format
print("This is the first value:{} and this is second key value:{}".format("(I'm One)","(I'm Two)"))
#or use key  {{}} in format can print {}
print("This test is add {{}} key{0},and second{1}".format("(First)","(Second)","(Third)"))
# not numeric key print
print("This key is not numeric: {food}, and this is not numeric key too:{color}".format(food="Apple", color='Blue'))
# multi type key
print("This is first:{0},this is tow:{1}, and this is by key{food}".format("first","second",food="apple"))
"""
print("This is first:{0},this is tow:{1}, and this is by key{food}".format(food="apple","first","second")) ==> error
print("This is first:{0},this is tow:{}, and this is by key{food}".format("first","second",food="apple")) ==> error second no key
"""
#'!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr()) can be used to convert the value before it is formatted:
x='中文'
print("Ascii:{!a}".format(x))  #Ascii:'\u4e2d\u6587'
print("Str:{!s}".format('\u4e2d\u6587'))  #Ascii:'\u4e2d\u6587'

# if want print multi dimension
table={"Jon":11122,"Tony":5555,"Peter":3333}
print("Tony:{0[Tony]:d}, peter:{0[Peter]:5d}, Jon:{0[Jon]:10d}".format(table)) # in [] didn't need simple quote


