

class T():

	def __init__(self, name):
		self.name = name
		self.age = 0
		
	def getName(self):
		return self.name
	
	def setName(self,n):
		self.name = n
		
	def getAge(self):
		return self.age
	
	def setAge(self,a):
		self.age=a
		self.setName("newName")
	
if __name__ == "__main__":
	t1 = T("apple")
	t2 = T("banana")
	
	t2.setAge(20)
	
	print(t1.getName(),",",t1.getAge())
	print(t2.getName(),",",t2.getAge())
	