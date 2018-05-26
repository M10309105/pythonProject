#!/usr/bin/python3


import matplotlib.pyplot as mpt 

xaxis=[x for x in range(1,6)]

mpt.plot(xaxis, [100,200,400,800,1600], lw=5, label='line1')
mpt.plot(xaxis, [100,110,120,1300,150], 'r--', label='dash line')
mpt.plot(xaxis, [300,500,700,900,1100], 'gs', label='square line')
mpt.plot(xaxis, [800,850,1500,799,500], 'b^', label='triangle dot')

mpt.xlabel('x lable')
mpt.ylabel('y label')
#mpt.title('this is testing')
mpt.legend()
mpt.show()