#/usr/bin/python3
#
#data structure
print("=" * 100)
print("5.1 List")
print("=" * 100)

l = list(range(10))
print(l)

l.append(11)
print(l)
l2 = list(range(15,21))
l.append(l2)
print(l)
#extand iterable item
l.extend(l2)
print(l)
l.insert(0,'a')
print(l)
#remove the first value equal given, return valueErr if not found
l.remove(15)
print(l)
#pop can specific index
print(l.pop(12))
print(l)
#clear equals del l[:]
del l[0:3]
#print(l)
#l.clear()
print(l)
#get index of the value which first match, or return valueErr
print(l.index(17))
#or search given range
print(l.index(17,4,15))
#print the value match times
print(l.count(1111))
#sort(*,key=none, reverse=False)
l.sort(reverse=True)
#some method return default None
print(l.sort()) 
print(l)
l.reverse()
print(l)
#list copy : shadow copy
l.append(l2)
l3=l.copy()
l4=l
del l[-1][5]
print("l: ",l, id(l), "l[0] id: ", id(l[0]))
#l4 have same address
print("l4: ",l4, id(l4), "l4[0] id: ", id(l4[0]))
#index 0 ipaddress still same
print("l3: ",l3, id(l3), "l3[0] id: ", id(l3[0]))

print("=" * 100)
print("5.1.1 List implement stack")
print("=" * 100)
#first in last out, using append() and pop
stack = list(range(11))
print(stack)
stack.append(199)
print(stack)
stack.pop()
print(stack)

print("=" * 100)
print("5.1.2 List implement queue")
print("=" * 100)
#you can use insert() and pop, but low efficiency
#or use collections.deque, can input and output faster
from collections import deque
queue = deque(list(range(10)))
print(queue)
print(queue.append(100), "queue:", queue)
print(queue.popleft(), "queue:", queue)

print("=" * 100)
print("5.1.3. List Comprehensions")
print("=" * 100)
#more simple generate complex list
test = []
for i in range(10):
    test.append(i**2)
print(test)
# need a range iterable object
#use lambda
test = list(map(lambda x: x**2, range(10)))
print(test)
#or
test = [x**2 for x in range(10)]
print(test)

test = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(test)

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([x for inside in vec for x in inside])

print("=" * 100)
print("5.1.4 List Comprehensions")
print("=" * 100)
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
print(matrix)
#change 
print([[row[i] for row in matrix] for i in range(4)])

#use built-in functions 'zip' have good efficiency
print(list(zip(*matrix)))