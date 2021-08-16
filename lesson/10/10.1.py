#/usr/bin/python3
#
#Class
print("=" * 100)
print("10.1 Operation System interface")
print("=" * 100)

#os modules provides dozens of function for interacting with the operating system
import os
print(os.getcwd())
#change working dir
os.chdir('C:\\Users\\Francis_Lin\\Desktop')
#system command
print(os.system("dir"))

#Be sure to use the import os style instead of from os import *. This will keep os.open() from shadowing the built-in open() function which operates much differently.

print("=" * 100)
#get list of all module functions in os
print(dir(os))
print("=" * 100)

#help
#help(os)
print("=" * 100)
import shutil
#daily file and directory management tasks useful tooles

# shutil.copyfile('data.db', 'archive.db')
# shutil.move('/build/executables', 'installdir')