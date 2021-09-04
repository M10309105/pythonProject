#/usr/bin/python3
#
#Class
print("=" * 100)
print("11.3 Working with Binary Data Record Layouts")
print("=" * 100)

import struct
#pack unpack

with open('myfile.zip', 'rb') as f:
    data = f.read()