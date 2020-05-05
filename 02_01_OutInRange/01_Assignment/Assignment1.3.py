#!/usr/bin/ev python
'''
Assignment1.3.py
'''
import random
def FlipCoin():
    ''' Simulate the flip of a coin '''
    if random.randrange (0, 2) == 0:
        return 'tails'
    return 'heads'

def GetHeadsInARow (numHeads):
    ''' Flips coins until it gets 3 heads in a row '''
    heads = count = 0
    while heads < numHeads:
        count += 1
        if FlipCoin () == 'heads':
            heads += 1
        else: # tails
            heads = 0
    return count

def main():
    ''' Driver for the GetHeadsInRow '''
    total = 0
    MAX_ROLL = 100.0
    numHeads = 3
    for n in range (int(MAX_ROLL)):
        flips = GetHeadsInARow (numHeads)
        total += flips
    
    print ('It took %.1f coin flips to get %d in a row.' % ((total/MAX_ROLL), numHeads))

main()
'''
1.3. Write a function that flips a coin; it returns “heads” or “tails”. 
Use that function to write a GetHeadsInARow function that accepts the number of heads to roll in a row 
before you return with total rolls it took to get that number of heads in a row.
'''