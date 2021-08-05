#/usr/bin/python3
#
#Exception
print("=" * 100)
print("8.8 pre defined clean action")
print("=" * 100)

#file handler not close
for line in open("lesson/7/test.txt"):
    print(line,end="\t")
    
print("=" * 100)

#this way better
with open("lesson/7/test.txt") as f:
    for line in f:
        print(line,end="\t")