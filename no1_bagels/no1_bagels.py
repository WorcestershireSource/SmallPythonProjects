import random

# Bagels - exercise one from the big book of small python programmes
# A programme which asks the user to use a random number and gives feedback based on their guesses
#Tags: short, game, puzzle

def main():
    # Get user input
    check = True
    while check == True:
        digits = input('How many digits to use? ')
        if digits.isdigit() == True:
            check = False
        else:
            print('Please input a number')

    int_digits = int(digits)

    # Generate a random three digit number as a string
    random_num = []
    for i in range(int_digits):
        random_num.append(str(random.randint(0, 9)))
        
    print(random_num)

    # Get guessses from user
    while True:
        fermi = 0
        pico = 0
        user_guess = input('What is your guess? ')
        guess_length = len(user_guess)
        if guess_length != int_digits:
            print('Your guess should be {} digits long'.format(digits))
        else:
            for i in range(int_digits):
                if random_num[i] == user_guess[i]:
                    fermi += 1
                elif random_num[i] in user_guess:
                    pico += 1
                    print('Pico')
            if fermi == int_digits:
                print('You got it!')
                new_game = input('Do you want to play again? y/n: ')
                if new_game == 'y':
                    main()
                else:
                    return
            else:
                for i in range(fermi):
                    print('Fermi')
            if pico == 0 and fermi == 0:
                print('Bagels')
    

if __name__ == '__main__':
    main()
