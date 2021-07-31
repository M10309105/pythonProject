#/usr/bin/python3
#
#package import
print("=" * 100)
print("6.4.1 import *")
print("=" * 100)

#   for directory example in 6.4.py if use import xxx.* like

#from sound.effects import * 

#   will import all in sound.effects, it will take more time and will occure something err
#   or the package defind __all__ list in __init__.py to decition what item will be imported in import *
#   for example sound/effects/__init__.py
__all__ = ["echo", "surrond","reserve"]

#   when use from sound.effects import * will improt "echo", "surrond","reserve"

