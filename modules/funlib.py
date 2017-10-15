# for module testing 

def showStar(a):
	if a<0 or a >100:
		print("illegal parameter")
		return -1
	starCount = a*2-1
	spaceCount = a - 1
	for i in range(0, starCount, 2):
		printSpace(a)
		printStar(i+1)
		a-=1



def printStar(a):
	while a >0:
		print("*",end="")
		a-=1
	print("")

def printSpace(a):
	while a > 0:
		print(" ",end="")
		a-=1