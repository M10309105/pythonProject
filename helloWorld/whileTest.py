#encoding: utf-8
#費氏數列、黃金分割數列
f0,f1,b=0,1,0
while b<=10:
	f0,f1,b=f0+f1,f0,b+1
	print(f0)