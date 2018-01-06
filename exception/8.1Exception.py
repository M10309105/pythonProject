#!python
#8.1 exception

import logging
import sys
import json

try:
	a = 1/0
except Exception as e:
	print("ERROR:{0}".format(e))
	logging.exception(e)
	#print(sys.exc_info())


print('####8.4#####')
#8.4
#raise error
try:
	a = 2/1
	b = 1/0
except Exception as e:
	raise NameError("HI It's me !")
	raise
else:
	print("a is {0}".format(a))