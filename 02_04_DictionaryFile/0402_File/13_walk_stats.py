#!/usr/bin/env python
"""Here is a demonstration of using os.path.walk to accumulate 
statistics through the files walked."""
import os
import total_text

def TotalDeep(stats, dir_name, files):
    """Called by walk to return statistics into stats.
    stats = [number_of_files, total]"""
    print ('TotalDeep() is called by main(): ')
    print (dir_name, "so far: %d files, adding to %d." % (stats[0], stats[1]))
    for file_name in files:
        pname = os.path.join(dir_name,file_name)
        if not os.path.isfile(pname):
            continue
        try:
            open_file = open(pname)
            for line in open_file:
                stats[1] += total_text.TotalText(line)
            open_file.close()
            stats[0] += 1
        #except IOError, msg:
        except IOError as msg:
            print (pname, msg)

def main():
    """stats is passed into walk for accumulating statistics.  Note that
    stats must be mutable for this to work."""
    stats = [0, 0]  # number_of_files, total
    # on Windows, my funcitons are not supported. 
    # https://docs.python.org/2/library/os.path.html
    os.path.walk('cats', TotalDeep, stats)
    print ('Call os.walk():')
    # https://www.tutorialspoint.com/python/os_walk.htm
    # for root, dirs, files in os.walk(".", topdown=False):
    #os.walk('cats', TotalDeep, stats)
    print ("That's %d files, totaling to %d." % tuple(stats))

if __name__ == '__main__':
    main()

"""
$ walk_stats.py
cats so far: 0 files, adding to 0.
I can't read 'cats/wrong_permissions'.
cats/deep_cats so far: 3 files, adding to 12.
cats/deep_cats/deeper_cats so far: 5 files, adding to 24.
That's 7 files, totaling to 36.
$ """