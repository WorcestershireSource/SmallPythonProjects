import random
import datetime


CYCLES = 100000

# Birthday analysis - a monte carlo modelling tool to assess the probability of a group of people sharing a birthday

def main():
    print()
    print('''This programme performs a monte carlo simulation to assess the probability 
that two or more people share a birthday in a group of a certain size''')
    print()

    # Get size of group from user
    print('How many birthdays should I generate? (Max 100)')
    while True:
        tmp = input('>')
        if tmp.isdecimal() and (1 < int(tmp) <= 100):
            size = int(tmp)
            break
    print()
    
    # Print an example list and the duplicate birthdays
    bday_list = birthday_gen(size)
    
    print('From a single simulation, here are {} random birthdays: '.format(size))
    for item in bday_list:
        print(item.strftime('%d %b. '), end='')
    print()
    
    # Check for joint birthdays
    j_bdays = joint_bday(bday_list)
    print('In this simulation, ', end='')
    if not j_bdays:
        print('there are no joint birthdays.')
    else:
        print('multiple people have a birthday on: ')
        for i in range(len(j_bdays)):
            print(j_bdays[i].strftime('%d %b. '), end='')
    print()
    print()
    
    # Run simulations 
    print('Generating {} random birthdays {} times'.format(str(size), str(CYCLES)))     
    tracker = 0
    for i in range(CYCLES):
        if i % 10000 == 0:
            print('{} simulations run...'.format(i))
        temp = len(joint_bday(birthday_gen(size)))
        if temp > 0:
            tracker += 1
    print('{} simulations run.'.format(CYCLES))
    print()
    print('Out of {} simulations of {} people, there was a matching birthday {} times'.format(str(CYCLES), str(size), str(tracker)))
    probability = tracker / CYCLES * 100
    print('This means that {} people have a {} per cent chance of having a matching birthday in their group.'.format(str(size), str(probability)))
    


    
def joint_bday(bday_list):
    duplicates = []
    for item in bday_list:
        if bday_list.count(item) > 1:
            duplicates.append(item)
    # Deduplicate by turning into a dictionary and back
    duplicates = list(dict.fromkeys(duplicates))
    return duplicates


def birthday_gen(size):
    birthdays = []
    for i in range(size):
       day_of_year = datetime.date(2000, 1, 1) + datetime.timedelta(random.randint(0, 364))
       birthdays.append(day_of_year)
    return birthdays

if __name__ == '__main__':
    main()
