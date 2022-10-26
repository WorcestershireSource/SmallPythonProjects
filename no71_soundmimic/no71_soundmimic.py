
import random, time, sys
try:
    import playsound
except ImportError:
    ('The playsound module is required to run this programme')
    sys.exit(1)

LETTERS = ['A', 'S', 'D', 'F']

def main():
    # Intro text
    high_score = 0
    while True:
        score = game_round()
        if score > high_score:
            high_score = score
        print()
        print('Your score was {}. The high score is {}'.format(score, high_score))
        print('Do you want to play again?')
        new_game = input('> ').lower()
        if new_game in ['no', 'n']:
            print('Thanks for playing')
            sys.exit(0)


def game_round():
    print('Try to memorise a pattern of ASDF letters (each with its own sound) as it gets longer and longer.')
    print('Press enter to begin')
    input()
    pattern = ''
    for i in range(1, 101):
        pattern = pattern + LETTERS[random.randint(0,3)]
        
        print('Pattern: ')
        for letter in pattern:
            print(letter)
            playsound.playsound('sound' + letter + '.wav')
        time.sleep(1)
        
        print('\n' * 60)
        print('What was the pattern?')
        answer = input('> ').upper()

        if answer == pattern:
            print('That\'s right!')
        else:
            print('Sorry - that\'s wrong - the pattern was {}'.format(pattern))
            return len(pattern) - 1


if __name__ == '__main__':
    main()

