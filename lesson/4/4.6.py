#/usr/bin/python3
#
#function

print("=" * 100)
print("define a function")
print("=" * 100)

def foo():
    print("This is foo")

foo()

def fib(n):
    a,b = 0,1
    while(a < n):
        print(a, end = ' ')
        a,b = b, a+b
    print()

fib(100)

print("=" * 100)
print("print a function, get address")
print("=" * 100)
print(fib)

print("=" * 100)
print("function default return None")
print("=" * 100)
print(fib(10))

print("=" * 100)
print("function return value")
print("=" * 100)

def fib2(n):
    a,b = 0,1
    result=[]
    while( a < n ):
        result.append(a)
        a , b = b , a + b
    return result
print(fib2(100))