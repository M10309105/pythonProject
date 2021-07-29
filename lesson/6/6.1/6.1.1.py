#/usr/bin/python3
#
#module
import foo
import sys
print("=" * 100)
print("6.1.1 Module")
print("=" * 100)

if __name__ == "__main__":
    foo.foo(sys.argv[1])

#python .\lesson\6\6.1\6.1.1.py "This is argument"
#This is  foo foo function, input value n= This is argument