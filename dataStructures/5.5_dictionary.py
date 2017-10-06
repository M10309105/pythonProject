# python documnet 5-5 dictionary

#index by key , unordered
#del can delete value

#list(d.keys())  can get a list have keys
#sorted(d.keys()) can get an ordered key list

tel = {"Tom":5559, "Peter": 55666, "Joy": 333}
tel["Bob"]=3337
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print(tel.values())
print(sorted(tel.values()))
print("Tom" in tel)  # if have key "Tom" return true

#dict  constructor builds dictionaries
print(dict([("a",5),(77,1234)]))
tt = {x: x**2 for x in (2,4,6,8)}
print(tt)

#5-6 looping  use items()
food = {"apple":"taste sweet", "banana":"smell good"}
for k, v in food.items():
	print(k,v)

#use enumerate() can get index
for k,v in enumerate(food.keys()):
	print(k,v)

#if want to pair two sequence use zip()
question = {"name","age","favorite color"}
answer = {"Bob",20,"blue"}
for q,a in zip(question,answer):
	print("what is your {0}? It is {1}".format(q,a))  #use "." to binding

#sequence reverse ==> reversed()
for i in reversed(range(1,10,2)):
	print(i)

