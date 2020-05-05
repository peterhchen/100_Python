#!/usr/bin/env python
"""soccer_team.py with getattr and setattr, as much as possible."""
import sys 
from soccer_team import * 
this_module = sys.modules[__name__]

def ProcessTeam(stream):
    print ('01_GetSetAttr_lab12_1.ProcessTeam():')
    global positions
    positions = []
    for line in stream:
        line = line.strip()
        if not line:
            continue
        # line => Forwards:, line => 7 Bruce Penge
        if line.endswith(':'):
            position = line[:-1]       #print ('line:', line); print ('line[:-1]:', line[:-1])
            setattr(this_module, position, [])
            positions += [position]    #print ('positions:', positions)
            continue
        #print ('line:', line)
        details = line.split(' ', 1)
        print ('details:', details)    # details => ['7', 'Bruce Penge']
        #print ('this_module:', this_module); print ('position:', position); print ('[details]:', [details])
        setattr(this_module, position,
                getattr(this_module, position) + [details])
        # Yeh Bruce Peng2 #7 Go for the goal!
        print ('Yeh %s #%s ' % (details[1], details[0]) + \
            getattr(this_module, "Notify%s" % position)())
    return stream.name, positions

def PrintTeam(team_name, positions):
    #print ('01_GetSetAttr_lab12_1.PrintTeam():')
    print (team_name + ':')
    #print ('positions:', positions) # ['Forwards', 'Midfielders', 'Defenders', 'Goalies']
    for each in positions:
        print ('  %s:' % each)
        #print ('this_module:', this_module) #<module '__main__' from '01_GetSetAttr_lab12_1.py'>
        for player in sorted(getattr(this_module, each)):
            # print ('each:', each + ';' + 'getattr(this_module, each):', getattr(this_module, each))
            # each: Forwards; getattr(this_module, each): [['7', 'Bruce Penge'], ..., ['6', 'Juvenal Ramirez']]
            print ('    ' + ': '.join(player))

def main(team_name = "Bees"):
    print ('01_GetSetAttr_lab12_1.main():')
    team_name, positions = ProcessTeam(open(team_name))
    PrintTeam(team_name, positions)

if __name__ == '__main__':
    print ('01_GetSetAttr_lab12_1: __main__')
    # call soccer_team() to get main()
    main()

""" Same output as soccer_team.py"""