# 4.6 function define
#Hanoi Tower


def fin(n,reminder="finished!"):
	a,b = 0,1
	while a < n :
		print(a,end=" ")
		a,b=b,a+b
	print(reminder)

fin(5000)


def tower(index, _from, temp, to):
	if index == 1:
		print("put index ",index," from ",_from," to ",to)
	else:
		tower(index-1,_from,to,temp)
		print("put index ",index," from ",_from," to ",to)
		tower(index-1,temp,_from,to)

	
tower(3,"A","B","C")
print("""

""")
c=0
def towerByCount(index, _from, temp, to):
	global c
	if index == 1:
		c+=1
		print("Step(",c,")put index ",index," from ",_from," to ",to)
	else:
		towerByCount(index-1,_from,to,temp)
		c+=1
		print("Step(",c,")put1 index ",index," from ",_from," to ",to)
		towerByCount(index-1,temp,_from,to)
		

towerByCount(5,"A","B","C")
print("Total step in 5 layers of Hanoi Tower:",c)

print()
"""
When a final formal parameter of the form **name is present, it receives a dictionary (see Mapping Types — dict)
 containing all keyword arguments except for those corresponding to a formal parameter. 
 This may be combined with a formal parameter of the form *name (described in the next subsection) 
 which receives a tuple containing the positional arguments beyond the formal parameter list. (*name must occur before **name.)
"""
def moreTest(*name,**dict):
	for arg in name:
		print(arg)
	print()
	print("="*50)
	
	keys = sorted(dict.keys())
	for k in keys:
		print(k,":",dict[k])
		
moreTest("this is name1","name2","name3","nameN",Name="Tom",Age=50,gender="male",phone="0987654321")
