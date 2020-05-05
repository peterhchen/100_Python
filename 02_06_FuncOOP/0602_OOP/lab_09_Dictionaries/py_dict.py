#!/usr/bin/env python
"""
Improved dictionary implementation for demonstrating a Python
dictionary - the one shown in the video is py_dict_from_video.py.

It was not a good idea, and it is never a good idea, to have global
data, this causes a problem in the exercise where this module is
imported with the 'from' keyword.

A global dictionary is never needed because when a dictionary is
passed into a function, and is changed in the function, the change
is seen by the calling function.  That's a big benefit of mutable
data types.
"""

def SetUpPyDict():
    py_dict = {}   # empty dictionary

    # initializing a dictionary

    py_dict2 = {'break':'break from a loop and skip the else',
                'continue':'go to the next iteration',
                'for':'set up looping'}

    # Updating py_dict1 with py_dict2's keys and values.  
    # If py_dict2 has keys already in py_dict, py_dict2's
    # values will replace the old values for the key.

    py_dict.update(py_dict2)    

    # And you can just add an entry

    py_dict['pass'] = 'throw the ball'

    # If you add an entry with a duplicate key, the new 
    # meaning will be the one that sticks:

    py_dict['pass'] = 'do nothing'

    return py_dict


def CollectEntries(py_dict):
    """Collects a bunch of new entries for the dictionary"""
    while True:
        word = input('Word: ')
        if not word:
            return
        meaning = input('Meaning: ')
        py_dict[word] = meaning

def FindDefinitions(py_dict):
    """Reports a key:value pair for a given key"""
    while True:
        word = input('Word to find: ')
        if not word:
            return
        try:
            print ('%s : %s' % (word, py_dict[word]))
        except KeyError:
            print ('%s is not in the dictionary.' % word)

def MakePrompt(choices):
    choice_list = sorted(choices)
    guts = ', '.join(['(%s)%s' % (choice[0], choice[1:])
                      for choice in choice_list])
    return 'Choose ' + guts + ' (enter to quit) '

def PrintEntries(py_dict):
    """Prints out the dictionary entries, sorted by key"""
    for word in sorted(py_dict):
        print ('%s : %s' % (word, py_dict[word]))

def RunMenu(py_dict):
    """Runs the user interface for dictionary manipulation."""
    # The choices dictionary has function names for values.
    choices = {'add': CollectEntries, 'find': FindDefinitions,
               'print': PrintEntries}
    prompt = MakePrompt(choices)

    while True:
        raw_choice = input(prompt)
        if not raw_choice:
            break
        given_choice = raw_choice[0].lower()
        for maybe_choice in choices: 
            if maybe_choice[0] == given_choice:
                # The appropriate function is called
                # using the dictionary value for the name
                # of the function.    
                choices[maybe_choice](py_dict)
                break
        else:
            print ('%s is not an acceptible choice.' % raw_choice)

def main():
    py_dict = SetUpPyDict()
    RunMenu(py_dict)

if __name__ == '__main__':
    main()
"""
$ py_dict.py
Choose (a)dd, (f)ind, (p)rint (enter to quit) p
break : break from a loop and skip the else
continue : go to the next iteration
for : set up looping
pass : do nothing
Choose (a)dd, (f)ind, (p)rint (enter to quit) a
Word: yield
Meaning: return and start here with next call
Word: 
Choose (a)dd, (f)ind, (p)rint (enter to quit) f
Word to find: for
for : set up looping
Word to find: range
range is not in the dictionary.
Word to find: 
Choose (a)dd, (f)ind, (p)rint (enter to quit) 
$"""
