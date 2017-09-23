#for

words=["apple", "banana", "pineapple", "melon"]

print("print to a string split by _")
a='_'.join(words)
print(a)

"""#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
不換行 , end=""

"""
for w in words:
	print(w,end="")

print("""

	""")
print("if wnat get index use enumerate() function")

for index, w in enumerate(words):
	print("index ",index," is ", w)

	
print("if want to modify iterator elements, use slice [:]")
for w in words[:]:
	if len(w) > 6:
		words.insert(0,w)  #insert element to index 0 if length > 6

print(words)

print("""===============range()=======================
range(x)
range(start,end)
range(start,end,step)
	""")
	
for i in range(5,50,10):
	print(i)

print("use range() and len() can index the iterator, but usually use enumerate()")

for x in range(len(words)):
	print("index ",x," is ",words[x])

print()
print("break example ")

for x in range(5000):
	if(x > 10):
		break
	print(x)
	
	
print("""
pass example==> if language statement needs, but do nothing use pass""")

def passExample():
	pass


	
	
	
	
	
