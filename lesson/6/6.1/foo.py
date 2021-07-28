#/usr/bin/python3

def foo(n=100):
    print("This is ",__name__,"foo function, input value n=",n)

def _test(n=5):
    print("This is _test function")