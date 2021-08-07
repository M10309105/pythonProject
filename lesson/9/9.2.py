#/usr/bin/python3
#
#Class
print("=" * 100)
print("9.2 Python Scopes and Namespaces")
print("=" * 100)

#The important thing to know about namespaces is that there is absolutely no relation between names in different namespaces;
#use the word attribute for any name following a dot #  z.real, real is an attribute of the object z. Strictly speaking
#Attributes may be read-only or writable

#. The namespace containing the built-in names is created when the Python interpreter starts up, and is never deleted. The global namespace for a module is created when the module definition is read in
#The local namespace for a function is created when the function is called,   and deleted when the function returns or raises an exception that is not handled within the function  Of course, recursive invocations each have their own local namespace.


#A scope is a textual region of a Python program where a namespace is directly accessible. "Directly accessible" here means that an unqualified reference to a name attempts to find the name in the namespace.

"""
the innermost scope, which is searched first, contains the local names

the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names

the next-to-last scope contains the current module's global names

the outermost scope (searched last) is the namespace containing built-in names

 To rebind variables found outside of the innermost scope, the nonlocal statement can be used; if not declared nonlocal, those variables are read-only (
"""
print("=" * 100)
print("9.2.1 example")
print("=" * 100)

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)