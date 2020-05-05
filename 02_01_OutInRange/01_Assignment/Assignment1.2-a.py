import random

#!/usr/bin/ev python
'''
Assignment1.2-a.py
'''
def GetSeven ():
    dice = random.randrange(1, 7), random.randrange(1, 7)
    print ('%d and %d' % dice)
    if (dice[0] + dice[1]) == 7:
        print ('Get Seven')
        return True
    else:
        return False

def main():
    while True:
        if (GetSeven() == True):
            break

main()

'''
1.2.  Write a function, "GetSeven", that rolls two dice until the sum of the dice is seven. 
Your function should return the number of rolls it took to get that seven.
'''