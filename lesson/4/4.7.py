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


print("=" * 100)
print("4.7.4 Arbitrary Argument Lists")
print("=" * 100)
def foo74(file, sep, *arg):
    print(file,"will write:",sep.join(arg))
foo74("test file",'/','a','b','c')

#better   #only key word argument can use after *arg
def foo741(*arg,sep='/'):
    print("will write:",sep.join(arg))
foo741('a','b','c')
foo741('a','b','c',sep='-')

print("=" * 100)
print("4.7.5 Unpacking Argument Lists")
print("=" * 100)
print(list(range(3,6)))
l1 = [3,6]
#if argiments save in list, you can use * operator to unpacking the augument
print(list(range(*l1)))
def foo475(*args):
    print('argument:',','.join(args))
argList=['apple','banana','cat']
foo475(*argList)
#same with dict,use ** operator to unpacking the augument
def foo4751(*args):
    print('argument:',','.join(args))
dict1={'fname':'apple','cname':'banana','lname':'cat'}
def foo4751(**argList):
    for i in argList:
        print("{}:{}".format(i,argList[i]))
foo4751(**dict1)

print("=" * 100)
print("4.7.6  Lambda")
print("=" * 100)
#lambda return a function
foo=lambda x,y : x + y
print(foo(1,2))
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])  #sort tuple[1], return touple[1] to sort function
print(pairs)
print((lambda a,b,c : a+b*c)(1,2,3))


print("=" * 100)
print("4.7.7  function document setting")
print("=" * 100)
def foo4771():
    """This is document, need brief, end with'.'.

    And second line need empty.
    """
    pass
print(foo4771.__doc__)

print("=" * 100)
print("4.7.8  Function Annotations")
print("=" * 100)
def foo478(a1:str, a2:str='default')->str:
    print("Annotations:",foo478.__annotations__)
    return a1 + " and " + a2
print(foo478('AAA'))
print(foo478.__annotations__)

print("=" * 100)
print("4.8  coding style")
print("=" * 100)
print("using 4 space, not tab")
print("don't over 79 characters per line")
print("new line to sparater class or large block")
print("put annotation in single line")
print("add space between operator or (), but not inside=> a = f1(1 , 3) + f2(4 , 6)")
print("same class naming format, use UpperCamelCase")
print("use utf8 (default)")
print("don't use non-ASCII character when naming")
