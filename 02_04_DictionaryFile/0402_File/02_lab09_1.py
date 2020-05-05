#!/usr/bin/env python
"""Dictionary implementation for demonstrating a dictionary.
   ... with a new option will print out the dictionary 
   alphabetically by the meanings.
   This module imports from the py_dict.py.
   lab09_1_from_video.py is the previous module.
   """
from py_dict import *  # Careful of this!
def ListDefinitions(py_dict):
    """Prints out the dictionary, alphabetically by the
    meanings"""
    #print ("ListDefintions1:")
    defs = [] 
    for k, v in py_dict.items(): 
        defs += [(v, k)]
    # or: defs = [(v, k) for (k, v) in py_dict.items()]        
    defs.sort()
    for (v, k) in defs:
        print (v, ':', k)

# duplcate function definition. Python pick up the lastest one        
def ListDefinitions(py_dict):
    """Prints out the dictionary, alphabetically by
    the meanings -- implemented via the sort key option."""
    #print ('ListDefintions2: ')
    def ValueKey(k):
        return py_dict[k]

    for each in sorted(py_dict, key=ValueKey):
        print (py_dict[each], ':', each)

# Duplcate RunMenu defined in import. Python pick up the current one.
def RunMenu(py_dict):
    """Runs the user interface for dictionary manipulation."""
    choices = {'add': CollectEntries,
               'definitions': ListDefinitions,
               'find': FindDefinitions, 'print': PrintEntries}
    prompt = MakePrompt(choices)
    while True:
        raw_choice = input(prompt)
        if not raw_choice:
            break
        given_choice = raw_choice[0].lower()
        for maybe_choice in choices:
            if maybe_choice[0] == given_choice:
                choices[maybe_choice](py_dict)
                break
        else:
            print ('%s is not an acceptible choice.' % raw_choice)

def main():
    # setupPyDict() import from py_dict.py
    py_dict = SetUpPyDict()
    RunMenu(py_dict)

if __name__ == '__main__':
    main()
"""
$ lab09_1.py
Choose (a)dd, (d)efinitions, (f)ind, (p)rint (enter to quit) d
an object used to access a value in a dictionary : key
break out of a loop and skip the else : break
do nothing : pass
go to the next iteration of the loop : continue
Choose (a)dd, (d)efinitions, (f)ind, (p)rint (enter to quit) 
$
"""