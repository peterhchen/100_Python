#!/usr/bin/env python
"""shelve_dictionary.py
An improved version of shelve_dictionary that imports the improved
version of py_dict.py

"""
import shelve 

# a surgical import
import sys
if __name__ == '__main__':
    sys.path.insert(0, "..") 
else:                        
    sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))
from lab_09_Dictionaries.py_dict \
     import CollectEntries, FindDefinitions, MakePrompt, PrintEntries

def main():
    """Runs the user interface for dictionary manipulation."""

    choices = {'add': CollectEntries, 'find': FindDefinitions,
               'print': PrintEntries}
    prompt = MakePrompt(choices)

    try:
        py_dict = shelve.open("py_dict.dat")
    except IOError as msg:
        print ('File could not be opened.')
        return
    
    while True:
        raw_choice = input(prompt)
        if raw_choice == '':
            break
        given_choice = raw_choice[0].lower()
        for maybe_choice in choices:
            if maybe_choice[0] == given_choice:
                choices[maybe_choice](py_dict)
                break
        else:
            print ('%s is not an acceptible choice.' % raw_choice)

    py_dict.close()

if __name__ == '__main__':
    main()
"""
$ shelve_dictionary.py
Choose (a)dd, (d)efinitions, (f)ind, (p)rint (enter to quit) a
Word: key
Meaning: an object used to access a value in a dictionary
Word: break
Meaning: break out of a loop and skip the else
Word: 
Choose (a)dd, (d)efinitions, (f)ind, (p)rint (enter to quit) p
break : break out of a loop and skip the else
key : an object used to access a value in a dictionary
Choose (a)dd, (d)efinitions, (f)ind, (p)rint (enter to quit) 
$ shelve_dictionary.py
Choose (a)dd, (d)efinitions, (f)ind, (p)rint (enter to quit) p
break : break out of a loop and skip the else
key : an object used to access a value in a dictionary
Choose (a)dd, (d)efinitions, (f)ind, (p)rint (enter to quit) 
$
"""
