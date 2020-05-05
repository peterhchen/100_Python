#!/usr/bin/env python
"""lab12_1.py -- Adding up the file sizes in the current directory,
three ways, and comparing them."""
import os
#import subprocess
from subprocess import check_output
__pychecker__ = 'no-local'

def AccuracyTest():
    print ("AccuracyTest():")
    print ("os.listdir:", AddFilesOsListdir())
    print ("os.popen:  ", AddFilesOsPopen())
    print ("subprocess:", AddFilesSubprocess())

def AddFilesOsListdir():
    #print ("AddFilesOsListdir:")
    total = 0
    files = os.listdir('.')
    #print ('files:', files)
    for f in files:
        #print ('f:', f)
        if os.path.isdir('./' + f):
            continue
        #print ('f:', f, 'os.path.getsize():', os.path.getsize('./' + f))
        total += os.path.getsize('./' + f)
    return total

def AddFilesOsPopen():
    #return TotalLsSize(os.popen("ls -al"))
    #print ("AddFilesOsPopen:")
    return TotalLsSize(os.popen("dir"))

def AddFilesSubprocess():
    # return TotalLsSize(subprocess.Popen(["ls", "-al"], stdout=subprocess.PIPE).stdout)
    #https://stackoverflow.com/questions/14894993/running-windows-shell-commands-with-python
    #print ('AddFilesSunbprocess:')
    # All informaiton in one line. Too difficult to parsing in windows.
    return TotalShellSize(check_output("dir", shell=True).decode())  # change binary into string format.

def ProfileTest():
    print ('ProfileTest():')
    for i in range(100):
        AddFilesOsListdir()
        AddFilesOsPopen()
        AddFilesSubprocess()

def TotalLsSize(file_obj):
    total = 0
    for line in file_obj:
        #print ('line:', line)
        #print ('type (line):',type(line))
        tlist = line.split(' ')
        #print ('tlist:', tlist)
        if '<DIR>' in tlist: 
            continue
        # if line[0] == 'd':
        #     continue
        parts = line.split()
        # print ('parts', parts)
        # if len(parts) != 9:
        #     continue
        if len(parts) != 5:
            continue
        #total += int(parts[4])
        try:
            part=''
            if ',' in parts[3]:
                part = parts[3].replace(',', '')
            else:
                part = parts[3]
            #print ('part:', part)
            num = int(part)
            #print ('num:', num)
        except ValueError:
            pass
        else:
            total += num
    return total

def TotalShellSize(file_obj):
    total = 0
    # https://stackoverflow.com/questions/28842717/parsing-python-subprocess-check-output
    # how to parse byte-by-byte of check_output? 
    # for line in output.splitlines():
    for line in file_obj.splitlines():
        #print ('line:', line)
        #print ('type (line):',type(line))
        tlist = line.split(' ')
        #print ('tlist:', tlist)
        if '<DIR>' in tlist: 
            continue
        # if line[0] == 'd':
        #     continue
        parts = line.split()
        #print ('parts', parts)
        # if len(parts) != 9:
        #     continue
        if len(parts) != 5:
            continue
        #total += int(parts[4])
        try:
            part=''
            if ',' in parts[3]:
                part = parts[3].replace(',', '')
            else:
                part = parts[3]
            #print ('part:', part)
            num = int(part)
            #print ('num:', num)
        except ValueError:
            pass
        else:
            total += num
    return total

def main():
    AccuracyTest()
    import profile
    profile.run('ProfileTest()')

if __name__ == '__main__':
    main()
"""
$ lab12_1.py
os.listdir: 26298
os.popen:   26298
subprocess: 26298
         30376 function calls in 1.872 CPU seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      101    0.004    0.000    0.004    0.000 :0(WEXITSTATUS)
      101    0.012    0.000    0.012    0.000 :0(WIFEXITED)
      101    0.000    0.000    0.000    0.000 :0(WIFSIGNALED)
       77    0.004    0.000    0.004    0.000 :0(append)
      300    0.016    0.000    0.016    0.000 :0(close)
      200    0.012    0.000    0.012    0.000 :0(fcntl)
      100    0.004    0.000    0.004    0.000 :0(fdopen)
      100    0.068    0.001    0.068    0.001 :0(fork)
      200    0.012    0.000    0.012    0.000 :0(isinstance)
     5400    0.100    0.000    0.100    0.000 :0(len)
      100    0.032    0.000    0.032    0.000 :0(listdir)
      200    0.000    0.000    0.000    0.000 :0(pipe)
      100    0.108    0.001    0.108    0.001 :0(popen)
        1    0.000    0.000    0.000    0.000 :0(range)
      100    0.016    0.000    0.016    0.000 :0(read)
       78    0.004    0.000    0.004    0.000 :0(remove)
        1    0.004    0.004    0.004    0.004 :0(setprofile)
     5400    0.104    0.000    0.104    0.000 :0(split)
     5300    0.236    0.000    0.236    0.000 :0(stat)
      178    0.004    0.000    0.004    0.000 :0(waitpid)
        1    0.000    0.000    1.868    1.868 <string>:1(<module>)
      100    0.156    0.002    0.872    0.009 lab12_1.py:12(AddFilesOsListdir)
      100    0.024    0.000    0.440    0.004 lab12_1.py:21(AddFilesOsPopen)
      100    0.036    0.000    0.540    0.005 lab12_1.py:24(AddFilesSubprocess)
... The rest of the output is irrelevant.
It seems fishy that os.listdir() takes longer than both subprocess.Popen()
and os.popen().  Maybe somehow we are comparing apples and oranges?
$ """