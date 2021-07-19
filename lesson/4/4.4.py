#/usr/bin/python3
#break, continue


print("=" * 100)
print("break")
print("=" * 100)
for i in range(2,10):
    for j in range(2,i):
        if i % j == 0:
            print("{} equals {} * {}".format(i,j,i//j))  # '//' floor division
            break
    else:   # go to here if for itreate to end
        print(i,"is a prime number")

print("=" * 100)
print("continue")
print("=" * 100)
for i in range(2,10):
    if i % 2 == 0:
        print(i,"is even number")
        continue
    print(i,"is odd number")