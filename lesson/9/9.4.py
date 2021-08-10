#/usr/bin/python3
#
#Class
print("=" * 100)
print("9.4")
print("=" * 100)


#same variable in class, first use is object variable
class Warehouse:
    purpose = 'storage'
    region = 'west'

c1 = Warehouse()
print(c1.purpose, c1.region)
c2 = Warehouse
c2.purpose = "aaa"
print(c2.purpose, c2.region)

#function can defind outside, but user confuse
def foo(self,a):
    print("This is foo",a)

class Class1:
    f = foo
    #slef method invoke
    def g(self, a):
        self.f(a)
    
c3 = Class1()
c3.f(100)
c3.g(500)
print(c3.__class__)