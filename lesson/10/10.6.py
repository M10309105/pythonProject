#/usr/bin/python3
#
#Class
print("=" * 100)
print("10.6 Mathematics")
print("=" * 100)

#math

import math
print(math.pi)
print(math.pow(math.cos(1),2)+math.pow(math.sin(1),2))
print(math.log(1024,2))


#random
import random
print(random.choice([1,2,3,4,5]))
print(random.random())
print(random.randrange(10))

#statistics
import statistics
data = [1,5,2.65,55.2,46.2,12]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))