# Differs to the version in the book - runs a simulation of many games to show probabilities

import random
import time

def main():
    no_of_sims = get_input('How many simulations do you wan to run?', 10000000)
    no_of_doors = get_input('How many doors are in the game?', 100)
    print()
    
    simulation(no_of_sims, no_of_doors)



def simulation(no_of_sims, no_of_doors):
    outcomes = {'Stick wins': 0, 'Switch wins': 0, 'Both lose': 0, 'Total': 0}
    counter = time.time()

    for i in range(no_of_sims):
        if time.time() > counter + 4:
            print('{}% complete'.format(round((i / no_of_sims) * 100, 1)))
            counter = time.time()
        
        doors = ['Car']
        for j in range(no_of_doors - 1):
            doors.append('Goat') 

        random.shuffle(doors)

        first_choice = doors.pop()

        if doors[0] == 'Goat':
            host_door = doors.pop(0)
        elif doors[1] == 'Goat':
            host_door = doors.pop(1)
        else:
            print('Error')

        switch_door = doors.pop()
        
        if switch_door == 'Car':
            outcomes['Switch wins'] += 1
        elif first_choice == 'Car':
            outcomes['Stick wins'] += 1
        elif switch_door == 'Goat' and first_choice == 'Goat':
            outcomes['Both lose'] += 1

        
    print('In {} simulations with {} doors:'.format(no_of_sims, no_of_doors))
    print()
    print('STICKING with your first choice would mean winning in {} games or {}% of the time'.format(outcomes['Stick wins'], round(outcomes['Stick wins'] / no_of_sims * 100, 1)))
    print('SWITCHING would mean winning in {} games or {}% of the time'.format(outcomes['Switch wins'], round(outcomes['Switch wins'] / no_of_sims * 100, 1)))
    print('Both strategies would have lost in {} games or {}% of the time'.format(outcomes['Both lose'], round(outcomes['Both lose'] / no_of_sims * 100, 1)))
    print()
    print('OUTCOME - NUMBER - PERCENTAGE')
    for item in outcomes:
        if item != 'Total':
             outcomes['Total'] += outcomes[item]
        
        print('{} - {} - {}%'.format(item, outcomes[item], round(outcomes[item] / no_of_sims * 100, 1)))
    print()


def get_input(text, max):
    print(text, ' (Max {})'.format(max))
    while True: 
        value = input('> ')
        if value.isdecimal():
            value = int(value)
            if value <= max:
                return value
        print('Not a valid input')
        print()
    
if __name__ == '__main__':
    main()






        

