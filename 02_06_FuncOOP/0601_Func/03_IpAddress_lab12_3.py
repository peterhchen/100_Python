#!/usr/bin/env python
"""lab12_2.py  Reports the ip address of this machine.
Linux only."""
#import subprocess
from subprocess import check_output

def GetIP():
    # output = subprocess.Popen("/sbin/ifconfig",
    #                           stdout=subprocess.PIPE).stdout
    output = check_output("ipconfig", shell=True).decode()
    # https://stackoverflow.com/questions/28842717/parsing-python-subprocess-check-output
    # how to parse byte-by-byte of check_output? 
    # for line in output.splitlines():
    #print ('output:', output)
    for line in output.splitlines():
        #print ('line:', line)
        #address_at = line.find("inet addr:")
        address_at = line.find("IPv4 Address")
        #print ("address_at:", address_at)
        if address_at == -1:
            continue
        #return line[address_at + 10:].split()[0]
        return line[address_at + 35:].split()[0]
    
if __name__ == '__main__':
    print (GetIP())

"""
$ lab12_2.py
10.0.0.153
$
"""