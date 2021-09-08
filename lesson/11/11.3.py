#/usr/bin/python3
#
#Class
print("=" * 100)
print("11.3 Working with Binary Data Record Layouts")
print("=" * 100)

import struct
#pack unpack

with open('myfile.zip', 'rb') as f:
<<<<<<< HEAD
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
=======
    data = f.read()
>>>>>>> 7f50301741137947778fa1af17a75ea0e8127bd6
