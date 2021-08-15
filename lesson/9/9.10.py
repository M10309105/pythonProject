#/usr/bin/python3
#
#Class
print("=" * 100)
print("9.9 Generator Expressions")
print("=" * 100)

 #Generator expressions are more compact but less versatile than full generator definitions and tend to be more memory friendly than equivalent list comprehensions.

print(sum(i*i for i in range(10)))

data = 'golf'
print(list(data[i] for i in range(len(data)-1,-1,-1)))
