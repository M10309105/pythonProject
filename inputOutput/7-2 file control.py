#!python3

#7-2 write and read files

#open can open the file  open(filename,mode))

with open('7.1 input output.py','r') as f :
	data = f.read()
f.close()

print("code:\n{0}\n\n".format(data))

with open('7.1 input output.py','r') as f :
	print('read one line:\n')
	for line in f:
		print("{0}".format(line))

f.close()

with open('test.txt','wb') as f:

f.close()



# json code

import json
json.dumps([1,2,3])

a = json.load(f)