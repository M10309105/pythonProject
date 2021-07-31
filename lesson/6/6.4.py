#/usr/bin/python3
#
#module
print("=" * 100)
print("6.4 package")
print("=" * 100)

#naming A.B means B is sub module in A
# sound/                          Top-level package
#       __init__.py               Initialize the sound package
#       formats/                  Subpackage for file format conversions
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  Subpackage for sound effects
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  Subpackage for filters
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py
#               ...

#when import package, python will search path from sys.path to find it 
#Ths direcroty in pachage must have an __init__.py file that python just know this directory is a package
#the __init__.py can be empty or do something init or setup __all__ variable

#you can import specific package like

#import sound.effects.echo 

#   and must call the full name when invoke then.

#sound.effects.echo.foo(xx,xx,xx=xx)

#   or the other way to import the function which you need

#from sound.effects.echo import foo

#   this way can skip the package prefix like

#foo(xx,xx,xx)

#   when use from xxx import aaa, the aaa can be function, class or variables defined in xxx
#   if aaa not find, will raise itemError
#  

