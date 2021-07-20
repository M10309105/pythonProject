#/usr/bin/python3
#function


print("=" * 100)
print("4.7.1 function default value")
print("=" * 100)
def ask_ok(msg, reties=4, reminder="only Yes or No"):
    while reties > 0:
        isOK = input(msg)
        if isOK in ('y','ye','yes'):
            return True
        if isOK in ('n', 'no', 'nope'):
            return False
        reties -= 1
    if reties == 0:
        raise ValueError("input error")
    print(reminder)

#ask_ok("hello, exit?:")
#ask_ok("hello, exit?:", 1)

print("list, dict default value only set once that will share the variable")
def foo(a, l=[]):
    l.append(a)
    return l
print(foo(1))
print(foo(2))
print(foo(3))
print("if dont want share default value")
def foo2(a,l=None):
    if l is None:
        l=[]
    l.append(a)
    return l

print(foo2(1))
print(foo2(2))
print(foo2(3))
print("=" * 100)
print("4.7.2 keyword argument")
print("=" * 100)
def foo72(a,b=1,c=2):
    print("a={}, b={}, c={}".format(a,b,c))

foo72(100,c=50)
foo72(b=50,a=101)
#foo72(b=50,c=101) #will error brcause a not set

print("=" * 100)
print("multi argument (dict)")
def foo721(name, *arg1, **arg2):
    print("this is name value:",name)
    for i,v in enumerate(arg1):
        print("this is second argument(tuple): {}:{}".format(i,v))
    print('-' * 50)
    for i in arg2:
        print("this is third argument(dict): {}:{}".format(i,arg2[i]))

foo721("hello", "This is arg2-1", "This is arg2-2", "This is arg2-3", arg31="arg3-1 value", arg32="arg3-2 value", arg33="arg3-3 value")

print("=" * 100)
print("4.7.3 special argument")
print("=" * 100)
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                - Keyword only
#          -- Positional only
#python 3.9 support position
def foo73(pos1, pos2, /, pos3, key1=100, *, key2=200):
    print("pos1:{}, pos2:{},  pos3:{},key1:{}, key2:{}".format(pos1,pos2,pos3,key1,key2))

#foo73(1,2,key1=200)  #err: miss pos3
foo73(1,2,key1=200,pos3=5) #pos3 can use keyword
foo73(1,2,3,key2=500)

def foo731(name, **kwds):
    return 'name' in kwds

#foo731(100, name=50) # will error, got multiple values for argument 'name' 
print(foo731(100, name1=50))