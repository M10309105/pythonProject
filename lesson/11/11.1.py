#/usr/bin/python3
#
#Class
print("=" * 100)
print("11.1 Output Formatting")
print("=" * 100)

#reprlib

import reprlib
# customized for abbreviated displays of large or deeply nested containers:
print(reprlib.repr(set('supercalifragilisticexpialidocious')))
print(set('supercalifragilisticexpialidocious'))

import pprint
arr = [[[1,2,3,['a','c','d']]],5,6,7,[(1,2,3),(4,6,7)]]
pprint.pprint(arr,width=10)

import textwrap
#format textarea screen size
doc = """The pprint module offers more sophisticated control 
over printing both built-in and user defined objects in a way 
that is readable by the interpreter. When the result is longer 
than one line, the “pretty printer” adds line breaks and indentation 
to more clearly reveal data structure:"""
print(textwrap.fill(doc,width=30))


#locale ?
import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
conv = locale.localeconv() 
print(conv)
x = 1234567.8
print(locale.format("%d", x, grouping=True))

print(locale.format_string("%s%.*f", (conv['currency_symbol'],conv['frac_digits'], x), grouping=True))