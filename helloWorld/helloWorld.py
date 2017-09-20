#encoding: utf-8
print ("hello world")	



print("a\tb")  #a    b
# use r before quote can be raw string
print(r"a\tb")   # a\tb


print("""three double quote or singo quote 
		can show new line in the string ,but use \\ can break warp text \ ...
		""")
		
word='hello world'

print(word[1])  #h
print(word[-1])  #d
print(word[2:5]) #llo

#list

list=[]
list1=[1,2,3,4,5]

list.append(1)   # or you can use +  ==>list1+[2,3,4]==>1,2,3,4,5,2,3,4
list.append(2)
list[:]=[]   #clear
list.append([1,2,3])
list.append([4,5,6])  #list==>  [[1,2,3],[4,5,6]]

print(len(list1))    #show list length
print(sum(list1))    #sum all elements  (all elements should be digital)
print(list1.count(2))  #count digital 2 occurrences
