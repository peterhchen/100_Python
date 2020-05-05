#!/usr/bin/env python
"""total_text.py provides a TotalText function, which adds up all the
numbers (2.0, 3.0, 87.0, 0.5, and etc.) in the text that it receives."""

import string  
punctuation_except_decimal = string.punctuation.replace('.', '')

def TotalText(text, total=0):
    """Returns the sum of all the numbers in the text."""
    words = text.split()
    for word in words:
        word = word.strip(punctuation_except_decimal)
        word = word.rstrip('.')
        try:
            num = float(word)
            #print ('num, word: ', num, word)
        except ValueError:
            pass
        else:
            total += num
    return total

def main():
    print ("Total =", end=" ")
    print (TotalText("""Here is 1. Add 2 makes 3 or maybe 12, 
depending on how you operate.

You might like 2.2 and that's enough unless you like "8.8" or 
maybe 1 more or maybe 87. . .5"""))
    
if __name__ == '__main__':
    main()

"""
$ total_text.py
Total = 117.5
$
"""