#/usr/bin/python3
#
#Exception
print("=" * 100)
print("8.5 Exception Chaining")
print("=" * 100)

def foo():
    raise IOError("This is IO test")

try:
    foo()
except Exception as e:
    raise RuntimeError("This is chaining message") from e

try:
    foo()
except Exception as e:
    raise RuntimeError("This is chaining message") from None
