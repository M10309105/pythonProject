#/usr/bin/python3
#
#Class
print("=" * 100)
print("10.5 String Pattern Matching")
print("=" * 100)

#regular expression

#re module

import re

find = re.findall(r'(?:\d{1,3})+',"172.1.0.100")
print(find)

#replace
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat cat in the the in hat'))

#simple string replace, just use replace()
print('This is apple'.replace('apple','banana'))