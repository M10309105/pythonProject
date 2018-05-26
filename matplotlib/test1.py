#!/usr/local/bin/python3

import matplotlib.pyplot as mpt


month1 = [1,2,3,4,5,6]
sales1 = [100,200,300,400,500,600]
sales2 = [600,500,400,300,200,100]


mpt.plot(month1,sales1,lw=10,label="test1")
mpt.plot(month1,sales2,'ro',label='test2') #ro: red o ,   r--: red --- line,   bs: blue squre, g^: green triangle
#mpt.axis([0,6,0,20]) # set plot x and y axis scale
mpt.plot(month1, [10,300,450,5,599,0],'b^',label='test3')# (line1-1,linr1-2,line1-3,line2-1,line2-2,line2-3)



mpt.xlabel('month')
mpt.ylabel('total')

mpt.legend()
mpt.title('test plot 1')
mpt.show()