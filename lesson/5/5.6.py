#/usr/bin/python3
#
#dict loop tips

print("=" * 100)
print("5.6 dict")
print("=" * 100)
#use items to get key and value
d1 = {'key1':'value1', 'key2':'value2','key3':'value3'}

for k,v in d1.items():
    print("{} : {} , {}".format(k,v,d1[k]))

#enumerate to get list index
for i,v in enumerate([5,6,7,8,9]):
    print(i, v)
print("=" * 100)
#use zip function if iterate two lists at same time
l1 = list(range(10))
l2 = [x**2 for x in list(range(10))]
l3 = [x**3 for x in list(range(10))]
for x,y,z in zip(l1,l2,l3):
    print(x,y,z)
print("=" * 100)
#reversed
for i in reversed(l3):
    print(i)
print("=" * 100)
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for i in sorted(basket):
    print(i)
print(basket)

#set can clear deduplication
for i in sorted(set(basket)):
    print(i)

#if wanna change list item value, create new one list is better
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filterList = []
for i in raw_data:
    if not math.isnan(i):
        filterList.append(i)
print(filterList)