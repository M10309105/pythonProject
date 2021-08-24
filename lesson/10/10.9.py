#/usr/bin/python3
#
#Class
print("=" * 100)
print("10.9 Data Compression")
print("=" * 100)

#zlib、gzip、bz2、lzma、zipfile 以及 tarfile。
import zlib
str = b'I have a pen, i have an apple, emm apple pen'
print(len(str))

compressStr = zlib.compress(str)
print(compressStr, len(compressStr))
print(zlib.decompress(compressStr))

print(zlib.crc32(str))