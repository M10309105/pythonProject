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