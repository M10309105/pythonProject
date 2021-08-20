#/usr/bin/python3
#
#Class
print("=" * 100)
print("10.4 Error Output Redirection and Program Termination")
print("=" * 100)

import sys

sys.stderr.write("This is stderr")

sys.exit()