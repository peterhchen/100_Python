#!/usr/bin/env python 
"""mod1.py  You can use ->   from module import *
   to bring all the attributes into your local namespace.
   But this is usually considered to be bad practice.
   You lose track of which attributes are local and are
   not local.  And, here's another problem.
"""
from mod1 import *
# will return 'None' since funciton Printx() does not have 'return' statement. 
# print ('Printx(): ', Printx())
print ('local version print (x): ', x)
print ('local version print (y): ', y)
print ('mod1 version Printx(): ')
Printx()
print ('mod1 version Printy(): ')
Printy()
print ("y[1] = 'a': ")
y[1] = 'a'
print ('Local version y: ', y)
print ('mod1 version Printy(): ')
Printy()  

print ('mod1 version Printx(): ')
Printx()

from mod1 import Printx, Printy
print ('mod1 version Printx():')
Printx()

# Note: from ... import ... does not allow 'mod1.x' assignment. 
# Only 'import mod1' worked.
#mod1.x = 3
import mod1
print ('mod1.x = 3')
mod1.x = 3
print ('Printx(): ')
Printx()
print ('mod1.Printx(): ')
mod1.Printx()

"""
>>> from mod1 import *
>>> Printx()
1
>>> x = 2
>>> Printx()    <-- gets mod1 version
1
>>> print x     <-- gets local version
2
>>> Printy()
[1, 2, 3]
>>> y[1] = 'a'  <-- a list is mutable!
>>> y
[1, 'a', 3]     <-- local version
>>> Printy()
[1, 'a', 3]     <-- mod1 version
>>> 
You can import certain attributes:
>>> from mod1 import Printx, Printy
>>> Printx()
1
>>> mod1.x = 3
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
NameError: name 'mod1' is not defined
>>> import mod1
>>> mod1.x = 3
>>> Printx()
3
>>> mod1.Printx()
3
"""