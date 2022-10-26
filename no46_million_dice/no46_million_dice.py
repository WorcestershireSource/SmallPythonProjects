# Million roll dice simulator 
# Shows the probabilities of different dice scores for a given number of dice by simulating a million rolls 

# Book version uses a dictionary to record the outcomes

import random
import time

ROLLS = 1000000

def main():
    print('Enter how many dice you want to roll (Max 40)')
    while True: 
        dice = input('> ')
        if dice.isdecimal() and int(dice) < 40:
            dice = int(dice)
            break
        print('Not a valid value, try again.')
    print()

    print('Simulating {} rolls of {} dice'.format(ROLLS, dice))
    print()


    outcomes = {}

    for i in range(dice, dice * 6 + 1):
        outcomes[i] = 0

    clock = time.time()    
    print('0% done')
    for i in range(ROLLS):
        if time.time() > clock + 1:
            print('{}% done'.format(round((i / ROLLS) * 100), 1))
            clock = time.time()
        
        score = 0
        for j in range(dice):
            score += random.randint(1,6)
        outcomes[score] += 1
    print('100% done')
    print()

    print('TOTAL - ROLLS - PERCENTAGE')
    for i in range(dice, dice * 6 + 1):
        print('{} - {} rolls - {}%'.format(i, outcomes[i], round((outcomes[i] / ROLLS) * 100, 1)))
    print()
    
    # # Simulate dice rolls and record outcomes in a list 
    # outcomes = []
    # for i in range(ROLLS):
    #     score = 0
    #     for j in range(dice):
    #         score += random.randint(1,6)
    #     outcomes.append(score)
    #     if i % 200000 == 0:
    #         progress = round((i / ROLLS) * 100)
    #         print('{}% done'.format(progress))
    # print('100% done')
    # print()
    # max = dice * 6

    # for i in range(2, max + 1):
    #     rolls_count = outcomes.count(i)
    #     per_cent = round(((rolls_count / ROLLS) * 100), 1)
    #     print('{} - {} rolls - {}%'.format(i, rolls_count, per_cent))
        
    
if __name__ == '__main__':
    main()
    


    

