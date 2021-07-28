#/usr/bin/python3
#
#module

print("=" * 100)
print("6.1 Module")
print("=" * 100)
import foo
foo.foo(200)
print(foo.__name__)

#import other way
#or from foo import * will import all functions except the function which name start with _
#from foo import foo
from foo import *
foo(50)
#can't access _xxx function
#_test()
#foo._test()

#or rename
from foo import foo as foo1
foo1('This is foo1')

#if using interative mode, the module only import once, or use importlib.reload(modulename)。
