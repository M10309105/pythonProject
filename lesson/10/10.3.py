#/usr/bin/python3
#
#Class
print("=" * 100)
print("10.3 Command Line Arguments")
print("=" * 100)

import sys
print(sys.argv)
print("=" * 100)
#argparse support more complex mechanism to process argv
#like perl getOpts
import argparse

parser = argparse.ArgumentParser(prog = 'top',
    description = 'Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)