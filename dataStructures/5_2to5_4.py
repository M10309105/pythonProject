#5-2 del

#del: delete list element or clear list
a=[1,2,3,4,5,6]

del a[0]
print(a)


#5-3 tuples and sequences

t=123,45,"a"
print(t)
u=t,(0,1,2,3)
print(u)
#5-4 Set

newSet={"a","b","c"} #or use set()
otherSet=set(["b","c","d"])
print(type(newSet))
print(newSet)
print(otherSet)
print(newSet | otherSet) # or 

a={x for x in 'abcddgafhxf' if x not in 'abcd'}
print(a)