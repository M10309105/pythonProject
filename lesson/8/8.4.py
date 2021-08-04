#/usr/bin/python3
#
#Exception
print("=" * 100)
print("8.4 raise exception")
print("=" * 100)

try:
    raise NameError("Test name")
except Exception as e:
    print(e)
    raise