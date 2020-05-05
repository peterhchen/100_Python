#!/usr/bin/env python
"""piper.py -- demonstrates running a shell-level command.  Stdout is
collected and piped into a file object which can be read as if it was
an open file.
"""
import sys

if __name__ == '__main__':
    sys.path.insert(0, "..") 
else:                        
    sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))
import apple.banana.total_text as total_text
import subprocess 

def Total_ps():
    """Returns the sum of all the numbers in a list
    of the processes running."""
                                                # On Windows,
    # open_pipe = subprocess.Popen(("ps", "-ef"), # use ["tasklist"]
    #                              stdout=subprocess.PIPE).stdout
    #print ('Total_ps()')
    open_pipe = subprocess.Popen(["tasklist"],
                                  stdout=subprocess.PIPE).stdout
    #print ('open_pipe:', open_pipe)
    try:
        #print ('open_pipe.read():', open_pipe.read())
        return total_text.TotalText(open_pipe.read())
    finally:
        open_pipe.close()
if __name__ == '__main__':
    print ("Your lucky number:", Total_ps())
"""
$ piper.py
Your lucky number: 1055528.0
$
"""
