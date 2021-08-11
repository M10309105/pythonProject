#/usr/bin/python3
#
#Class
print("=" * 100)
print("9.6 private variable")
print("=" * 100)


#using prefix '__' before variable name, for example: __name
#name mangling.(at least two _ in fornt of the variable, at most one _ after the variable)
#__name ==> _classname_name
#Name mangling is helpful for letting subclasses override methods without breaking intraclass method calls. For example:



class Mapping:
    def __init__(self, iterable):
        self.itemList = []
        self.__update(iterable)
    def update(self, iterable):
        for i in iterable:
            self.itemList.append(i)
    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):  
    def update(self,keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for i in zip(keys, values):
            self.itemList.append(i)

#__update method can be different if MappingSubclass want using __update
#Mapping: _Mapping__update
#MappingSubclass: _MappingSubclass__update





list1 = [1,2,3,4,5]
o1 = MappingSubclass(list1)
o1.update(range(5),range(5,10))
print(o1.itemList)



"""
Notice that code passed to exec() or eval() does not consider the classname of the invoking class to be the current class; 
this is similar to the effect of the global statement, the effect of which is likewise restricted to code that is byte-compiled together.
The same restriction applies to getattr(), setattr() and delattr(), as well as when referencing __dict__ directly.
"""