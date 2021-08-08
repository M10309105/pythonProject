#/usr/bin/python3
#
#Class
print("=" * 100)
print("9.3 class")
print("=" * 100)

#class
print("=" * 100)
print("9.3.1 class")
print("=" * 100)

class MyClass():
    pass
"""
<statement-1>
    .
    .
    .
    <statement-N>
"""

print("=" * 100)
print("9.3.2 class")
print("=" * 100)

class Car:
    """A simple example class"""
#init
    def __init__(self,type, color):
        self.type = type
        self.color = color

    def foo(self):
        print("This is Car.foo")

print(Car.__doc__)
car1 = Car("Big","red")
print(car1.type, car1.color)
