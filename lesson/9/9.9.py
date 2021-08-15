#/usr/bin/python3
#
#Class
print("=" * 100)
print("9.9 Generator")
print("=" * 100)

#generator is a tool for creating iterators. use yield to return the object.
#when generator invoke next() function, it will goto last leave point .
#generator will create __iter__() and __next__() function automatically

def reverse(data):
    for i in range(len(data)-1,-1,-1):
        yield data[i]
    
for char in reverse("This is apple"):
    print(char)
