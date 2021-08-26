#/usr/bin/python3
#
#Class
print("=" * 100)
print("10.10  Dates and Times")
print("=" * 100)

from timeit import Timer
print(Timer('t=a;a=b;b=t','a=1;b=2').timeit())

print(Timer('a,b=b,a','a=1;b=2').timeit())