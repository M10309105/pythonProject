#list 
#document from :https://docs.python.org/3.5/tutorial/datastructures.html#data-structures

def showList(list):
	print(list)


human=["Tom","Tony","Peter"]

human.append("Hen") #Add an item to the end of the list. Equivalent to a[len(a):] = [x].

human.extend(["Zoe","Flora","Tony"]) #Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

human.insert(len(human),"Bill") 
human.remove("Bill") # Remove the first item from the list whose value is x. It is an error if there is no such item.

print(human.pop(0)) #pop item , show item and remove it from list if no argument , return the last

print(human.index("Tony",2)) #index(x[, start[, end]]) Return zero-based index in the list of the first item whose value is x. Raises a ValueError if there is no such item.

bb=human.copy()  #Return a shallow copy of the list. Equivalent to a[:]. WHY shallow??????????????????????????????????? seem like deep copy

bb.remove("Tony")
showList(bb)
showList(human)
""""
#use list implements stack
list0=[1,3,5,7]
list0.append(9)
showList(list0)
print(list0.pop())

#implements queue
#use deque
from collections import deque
queue = deque["1","3"]
queue.append("5")
queue.append("7")
queue.popleft() #pop first elements
print(queue)
"""

queue = [x**2 for x in range(5)]
print(queue)

queue = [(x,y) for x in [1,2,3] for y in [5,1,2] if x!=y]
print(queue)

# List Comprehensions




