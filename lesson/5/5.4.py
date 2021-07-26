#/usr/bin/python3
#
#Sets
print("=" * 100)
print("5.4 Sets")
print("=" * 100)

set1 = {1,2,3,4,5}
print(set1)
print(1 in set1)
print(100 in set1)
for i in set1:
    print(i)

stringSet = set('This is set')
print(stringSet)

setingSet = {i for i in 'This is some centents bra bra bra' if i not in 'abcd'}
print(setingSet)