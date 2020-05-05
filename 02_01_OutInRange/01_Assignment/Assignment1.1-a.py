#!/usr/bin/ev python
'''
Assignment1.1-a.py
'''
def JudgeNumber (num):
    try:
        value = float (num)
    except TypeError:
        print ('Not a good number')
        pass
    else:
        return ('Good number %.1f.' % (value))

value = JudgeNumber (32)
print (value)
print (JudgeNumber (1.4))
print (JudgeNumber ("1"))

'''
1.1. Pay close attention to the specification and our style guide as you code these little functions. 
Use string formatting where appropriate. Test your functions and show the output.
a.  Write a function that receives a number and returns the number formatted to one decimal place as in the sentence:
Good number 32.2.
where the number that was received is placed in the sentence instead of the 32.2.

I named my function "JudgeNumber" because this label adheres to our style guide.

This line:

print JudgeNumber(32)
results in:

Good number 32.0.
written to stdout. While:

print JudgeNumber(1.4)
shows this on stdout:

Good number 1.4.
The function returns the string because the spec says it should. It does not print. 

Optional, and not part of the specification: what happens when you:

print JudgeNumber("1")
'''