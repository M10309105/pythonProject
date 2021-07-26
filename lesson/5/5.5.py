#/usr/bin/python3
#
#Dicts
#tuple can be a key in dictionary
print("=" * 100)
print("5.5 dict")
print("=" * 100)

tel = {'tom':1234567, 'tony':222345, 'jack':5556788}
print(tel)

del tel['tom']
print(tel)
print(list(tel))
print(sorted(tel))
print('tom1' in tel)
print('tom' not in tel)

print(dict([('key1','value1'),('key2','value2')]))
print(dict(key1='value1',key2='value2'))
print({x:x**2 for x in range(10)})