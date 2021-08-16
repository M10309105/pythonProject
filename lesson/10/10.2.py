#/usr/bin/python3
#
#Class
print("=" * 100)
print("10.2 File Wildcards")
print("=" * 100)

#like perl glob
import glob
files = glob.glob('lesson/*/*.py')
# files.sort()
for i in sorted(files):
    print(i)