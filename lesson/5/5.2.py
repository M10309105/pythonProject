#/usr/bin/python3
#
#del
print("=" * 100)
print("5.2 del")
print("=" * 100)

l = list(range(11))
del l[5]
print(l)

del l[5:]
print(l)

del l[:3]
print(l)

del l
#l is not defined
#print(l) 