import random

def GetSeven ():
    dice = random.randrange(1, 7), random.randrange(1, 7)
    #print ('%d and %d' % dice)
    if (dice[0] + dice[1]) == 7:
        #print ('Get Seven')
        return True
    else:
        return False

def GetAveSeven():
    sevenCnt = 0
    MAX_ROLL = 100
    for i in range(MAX_ROLL):
        if GetSeven() == True:
            sevenCnt += 1
            #print ("sevenCnt1: ", sevenCnt)
    #print ("sevenCnt2: ", sevenCnt)
    times = float(sevenCnt)/MAX_ROLL
    print ("Average Times to get 7 is %.2f " % times)
#!/usr/bin/ev python
'''
Assignment1.2-b.py
'''
def main():
    GetAveSeven()

main()

'''
1.2-b:
Write another function, "GetAveSeven", that calls GetSeven 100 times 
and reports the average number of times it took to get seven.
'''