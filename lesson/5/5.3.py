#/usr/bin/python3
#
#tuples and sequences
print("=" * 100)
print("5.3 tuples and sequences")
print("=" * 100)

t = 1,5,'aaa'
print(t)

u = t, 1
print(u)

u = t, (1,3,6,7,9)
print(u)

# Tuples are immutable:
try:
    u[0] = 1
except Exception as e:
    print(e)


t = ((1,2,3,4),(5,6,7,8),9)
print(t)

