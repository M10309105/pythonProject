#/usr/bin/python3
#
#Class
print("=" * 100)
print("9.5 inheritance")
print("=" * 100)

"""
class ClassName(BaseClass):
    ...

isintance(instance, class): can check object class name
issubclass(class A, class B): can check inheritance relationship
"""

class A:
    pass

class B(A):
    pass

a = A()
b = B()
#True
print(isinstance(b,B))
#True
print(isinstance(b,A))
#False
print(isinstance(a,B))
#True
print(issubclass(B,A))

print("=" * 100)
print("9.5.1 multi inheritance")
print("=" * 100)

class C:
    pass

#error if B or C is inheritance relationship
class D(B,C):
    pass

