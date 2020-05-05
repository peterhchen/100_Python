#!/usr/bin/env python
"""forRaneg01.py Inputs two integers and determines whether
the first is a multiple of the second. """

while True:  # True/False are keywords.   
    try:    
        number1 = int(input("Number please: "))
        break
    except ValueError:
        print ("Please try again.")
while True:
    try:
        number2 = int(input("Number please: "))
        break
    except ValueError:
        print ("Please try again.")
    
if number1 % number2 == 0:
    print ('%d is a multiple of %d' % (number1, number2))
else:
    print ('%d is not a multiple of %d' % (number1, number2))
"""
$ python forRange01.py
Number please: 8
Number please: 2
8 is a multiple of 2
$ python forRange01.py
Number please: 18
Number please: 17
18 is not a multiple of 17
$ """