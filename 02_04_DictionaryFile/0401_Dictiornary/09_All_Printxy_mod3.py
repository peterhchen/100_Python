#!/usr/bin/env python
"""mod3.py  __all__ specifies identifiers for export"""
from mod3 import *
print ('fromm mod3 import *:')
print ('dir(): ', dir())

from mod3 import x
print ('fromm mod3 import x:')
print ('x: ', x)
print ('Printy(): ', Printy())

import mod3 as other
print ('import mod3 as other:')
print ('otehr.x = 88')
other.x = 88
print ('other.Print():')
other.Printx()

"""
>>> from mod3 import *
>>> dir()
['__builtins__', '__doc__', '__name__', 'Printx', 'Printy']

>>> from mod3 import x
>>> x
1
>>> from mod3 import y
>>> y
[1, 2, 3]
>>> y[1] = 'hey'
>>> Printy()
[1, 'hey', 3]
>>> 

Another SAMPLE RUN:
>>> import mod3 as other
>>> other.x = 88
>>> other.Printx()
88
>>> 
"""