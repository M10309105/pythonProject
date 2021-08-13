#/usr/bin/python3
#
#Class
print("=" * 100)
print("9.8 iterators")
print("=" * 100)

for key in {'one':1, 'two':2}:
    print(key)

#the for will invoke function 'iter()' from container object  ("__iter__()")
#and this function have define '__next__()' function
#the exception 'StopIteration' will be raised when __next__() function get last item then stop the loop
#you can use next() to invoke __next__() function

s = "This is an apple"
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

print("=====implement iterator in your class===============")
class Reverse:
    """Iterator for looping over a sequence backwards"""
    def __init__(self,data):
        self.data = data
        self.index = len(data)

    #iter()
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index -= 1
            return self.data[self.index]

rev = Reverse("onion")
for i in rev:
    print(i)

