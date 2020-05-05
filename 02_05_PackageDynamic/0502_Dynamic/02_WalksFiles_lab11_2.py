#!/usr/bin/env python
"""lab11_2.py
Using os.walk to accumulate total through the files walked.

I'm running this code from my lab11 directory.

For this, I added two more __init__.py's in apple, and in work_here
so that the import facility would read the names (both directories
and .py files) in apple and find work_here; and because work_here
now has __init__.py it will read the names there and find lab11_1.py.

For lab11_1.py *only* the __init__.py in banana was needed.
"""

import os
import apple.work_here.lab11_1 as totaler 

def TotalDeep(starting_dir):
    """Returns (no_of_files, total) where no_of_files is the
    number of files founds in the directory structure starting at
    starting_dir, and total is the sum of all the numbers found in
    those files.
    """
    total = no_of_files = 0
    for this_dir, dir_names, file_names in os.walk(starting_dir):
        #print ("file_names: ", file_names)
        for this_file in file_names:
            #print ("this_dir:", this_dir, "this_file: ", this_file)
            path_name = os.path.join(this_dir, this_file)
            #print ("path_name: ", path_name)
            try:
                total += totaler.TotalFile(path_name)
                no_of_files += 1
                # print path_name, "so far: %d files, adding to %g" % (no_of_files, total)
            except IOError as msg:
                print (path_name, msg)
    return (no_of_files, total)

def main():
    #stats = TotalDeep('..')
    stats = TotalDeep('.')
    print ("That's %d files, totaling to %g." % stats)

if __name__ == '__main__':
    main()

"""
$ lab11_2.py
That's 1013 files, totaling to 21572143372.
$ """