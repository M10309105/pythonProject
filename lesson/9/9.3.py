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
        self.num = 0

    def foo(self):
        print("This is Car.foo, this car is",self.type,self.color,"car")

print(Car.__doc__)
car1 = Car("Big","red")
print(car1.type, car1.color)

print("=" * 100)
print("9.3.3 object")
print("=" * 100)

car1.num = 1
for i in range(10):
    car1.num = car1.num * 2
print(car1.num)
del car1.num

print("=" * 100)
print("9.3.4 method object")
print("=" * 100)
car1 = Car("Big","red")
car1.foo()


print("=" * 100)
print("9.3.5 Class and Instance Variables")
print("=" * 100)

car1 = Car("Big","red")
car2 = Car("small","green")
print(car1.type, car1.color)
print(car2.type, car2.color)

class TaxiCar(Car):
    #this is class variable
    passenger = []
    def __init__(self,type, color):
        self.type = type
        self.color = color
        #self obj
        self.passenger1 = []
    
    def getInto(self,passenger):
        self.passenger.append(passenger)

taxi = TaxiCar("big","yellow")
taxi.getInto("Tom")
taxi.getInto("Peter")
print(taxi.passenger)
taxi1 = TaxiCar("small","yellow")
taxi.getInto("Zoe")
print(taxi.passenger)