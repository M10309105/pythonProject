#/usr/bin/python3
#range

#range function 0 to n-1
print("=" * 100)
print("using range")
print("=" * 100)
for i in range(5):
    print(i)

print("=" * 100)
print("using range create list")
print("=" * 100)
list1 = list(range(5,10))
list2 = list(range(5))
list3 = list(range(0,16,3))
print("list1:",end='')
print(list1)
print("list2:",end='')
print(list2)
print("list3:",end='')
print(list3)

print("=" * 100)
print("using range and len to iterator list")
print("=" * 100)
for i in range(len(list3)):
    print(i,":",list3[i])

#range() function return not list obj but call iterable obj
print(sum(range(1,11)))