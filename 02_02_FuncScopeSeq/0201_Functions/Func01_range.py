#!/usr/bin/env python
"""Func01_range.py  How would you produce the following sequences using
the range operator?
      
        [3, 6, 9, 12]
        [-10, 210, 110]
        -1, -3, -5, -7,
"""
print (range(3, 13, 3))
print (range(-10, 211, 110))
for number in range(-1, -8, -2):
    print ("%d," % (number), end=" ")
print
"""
$ pyhton Func01_range.py
[3, 6, 9, 12]
[-10, 100, 210]
-1, -3, -5, -7,
$
"""