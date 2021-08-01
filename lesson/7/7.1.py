#/usr/bin/python3
#
#output
print("=" * 100)
print("7.1 output")
print("=" * 100)

year = 2021
month = '07'
v = 3.1415926
#(formatted string literals)
#https://docs.python.org/zh-tw/3/tutorial/inputoutput.html#tut-f-strings
print(f'This is format output {year:-10d}, {month:10}, v={v:.3f}')
#'!a' 會套用 ascii()，'!s' 會套用 str()，'!r' 會套用 repr()：

#str() vs repr()

print("=" * 100)
print("7.1.1 Formatted String Literals")
print("=" * 100)
import math
print(math.pi)
print(f'{math.pi:.3f}')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10} ==> 123')

#pad right
for name, phone in table.items():
    print(f'{name:>10} ==> {phone:<10} ==> 123')

print("=" * 100)
print("7.1.2 format method")
print("=" * 100)
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('We are the {1} who say "{0}!"'.format('knights', 'Ni'))
print('We are the {var1} who say "{var2}!"'.format(var2 = 'knights', var1 = 'Ni'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
#if dict
print('jack:{0[Jack]}'.format(table))

#or can ** to let table be pass by key word
print('jack: {Jack:d}'.format(**table))


print("=" * 100)
print("7.1.3 format method")
print("=" * 100)

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

#format to right
print('This is apple'.rjust(30))
print('This is apple'.ljust(30))
print('This is apple'.center(30))
print('This is apple'.zfill(30))

print("=" * 100)
print("7.1.4 old format")
print("=" * 100)
#% will be replaced
print('The value pi : %5.3f' % math.pi)