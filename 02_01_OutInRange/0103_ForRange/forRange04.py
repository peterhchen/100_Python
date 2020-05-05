#!/usr/bin/env python
""" Demonstrates a for loop """ 
numbers = range(5) 
print (numbers)
for num in numbers:
    print ("%d * 2 = %d" % (num, num * 2))
"""
OUTPUT:
$ for_loop.py
[0, 1, 2, 3, 4]
0 * 2 = 0
1 * 2 = 2
2 * 2 = 4
3 * 2 = 6
4 * 2 = 8

(rest of output is below)
"""