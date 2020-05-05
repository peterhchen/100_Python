#!/usr/bin/env python
"""lab06_3.py Sorts name strings by last name."""
NAMES = ["Jack Sparrow", "George Washington", "Tiny Sparrow",
         "Jean Ann Kennedy"]
def ReverseName(name):
    parts = name.split()
    return parts[-1] + ', ' + ' '.join(parts[:-1])
def main():
      # Separate into two lines are clearer
      sNames = sorted(NAMES, key=ReverseName)
      for name in sNames:
         print (ReverseName(name))
#    for name in sorted(NAMES, key=ReverseName):
#        print (ReverseName(name))
main()
"""
$ lab06_3.py
Kennedy, Jean Ann
Sparrow, Jack
Sparrow, Tiny
Washington, George
$
"""
