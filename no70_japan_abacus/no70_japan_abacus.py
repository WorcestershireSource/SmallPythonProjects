# Simulation of a traditional Japanese Abacus. Base 10 counting mechanism
# The single bead on the top (heaven) is worth 5 and the four on the bottom (earth) are worth 1 each
# The columns represent different base 10 values e.g. top bead in second column from the right = 50
# User can adjust individual beads using keyboard or provide a number to represent on the abacus

import sys
import copy

ABACUS_TEMPLATE = '''
   .  .  .  .  .  .  .  .  .  . 
+================================+
I  z  z  z  z  z  z  z  z  z  z  I
I  |  |  |  |  |  |  |  |  |  |  I
I  x  x  x  x  x  x  x  x  x  x  I
+================================+
I  c  c  c  c  c  c  c  c  c  c  I
I  v  v  v  v  v  v  v  v  v  v  I
I  b  b  b  b  b  b  b  b  b  b  I
I  n  n  n  n  n  n  n  n  n  n  I
I  m  m  m  m  m  m  m  m  m  m  I
I  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  I
+================================+

 + q  w  e  r  t  y  u  i  o  p
 - a  s  d  f  g  h  j  k  l  ;
'''
TEMPLATE_VALUES = ['+', '-', '=', ' ', 'I', '|']
UP_VALUES = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
DOWN_VALUES = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';']
HEAVEN_ROW_VALUES = ['z', 'x']
EARTH_ROW_VALUES = ['c', 'v', 'b', 'n', 'm', ',']
ABACUS_START_VALUES = {
    'z': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    'x': ['|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
    'c': ['|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
    'v': ['|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
    'b': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    'n': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    'm': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ',': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']   
}

def main():
    score = 0
    outcome = run_abacus(ABACUS_START_VALUES, score) 
    while True:
        abacus_values = outcome[0]
        score = outcome[1]
        outcome = run_abacus(abacus_values, score)


def run_abacus(abacus_values, score):
    score_copy = copy.deepcopy(score)
    score_as_list = [int(digit) for digit in str(int(score)).zfill(10)]

    # Print the abacus to the screen with the current scor
    for line in ABACUS_TEMPLATE.splitlines():
        counter = 0
        for i, char in enumerate(line):
            if char in TEMPLATE_VALUES or char in UP_VALUES or char in DOWN_VALUES:
                print(char, end='')
            elif char in HEAVEN_ROW_VALUES or char in EARTH_ROW_VALUES:
                print(abacus_values[char][counter], end='')
                counter += 1
            elif char == '.':
                print(score_as_list.pop(0), end='')
        print()
    print()

    # User amends the values and total is updated
    print('Enter a number, \'quit\' or adjust the value with the up/down keys')
    user_input = input('> ').lower()
    if user_input == 'quit':
        print('Exiting the programme.')
        sys.exit(0)
    elif user_input.isdecimal():
        score = float(user_input)
    else:
        for char in user_input:
            if char in UP_VALUES:
                x = UP_VALUES.index(char)
                score += 1 * pow(10, 9 - x)
            elif char in DOWN_VALUES:
                y = DOWN_VALUES.index(char)
                score -= 1 * pow(10, 9 - y)

    try:
        score_as_list = [int(digit) for digit in str(int(score)).zfill(10)]
    except ValueError:
        print('Negative values are invalid')
        return abacus_values, score_copy
   
    abacus_values = copy.deepcopy(ABACUS_START_VALUES)

    for i in range(10): # Decide which characters need to be amended to represent the number - make adjustments iteratively 
        if score_as_list[i] == 0:
            continue
        if score_as_list[i] >= 5:
            abacus_values['z'][i] = '|'
            abacus_values['x'][i] = 'O'    
        if score_as_list[i] in [1, 2, 3, 4, 6, 7, 8, 9]:
            abacus_values['c'][i] = 'O'
            abacus_values['b'][i] = '|'
        else: continue
        if score_as_list[i] in [2, 3, 4, 7, 8, 9]:
            abacus_values['v'][i] = 'O'
            abacus_values['n'][i] = '|'   
        else: continue   
        if score_as_list[i] in [3, 4, 8, 9]:
            abacus_values['b'][i] = 'O'
            abacus_values['m'][i] = '|'      
        else: continue   
        if score_as_list[i] in [4, 9]:
            abacus_values['n'][i] = 'O'
            abacus_values[','][i] = '|'    
    return abacus_values, score


if __name__ == '__main__':
    main()



# Realised this function could be designed out - changed the main function and merged two previous functions to simplify programme

#def get_totals(abacus_values):
#     col_totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # This variable stores totals for each column. Eleventh column is total (10 index)

#     for column in range(10):
#         if abacus_values['x'][column] == 'O':
#             col_totals[column] += 5
#             col_totals[10] += 5 * pow(10, (9 - column))

#     for column in range(10):
#         condition = True 
#         for row in EARTH_ROW_VALUES:
#                 if abacus_values[row][column] == 'O': 
#                     col_totals[column] += 1
#                     col_totals[10] += 1 * pow(10, (9 - column))
#                 elif abacus_values[row][column] == '|':
#                     break
            
#     return col_totals