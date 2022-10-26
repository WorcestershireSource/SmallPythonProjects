import sys
import random

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
SUITE = [HEARTS, DIAMONDS, CLUBS, SPADES]
CARD_NO = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

def show_cards(list_of_cards):
    for item in list_of_cards:
        print(' ___ ', end='')
    print()
    for item in list_of_cards:
        if item[0] == 10:
            print('|10 |', end='')
        else:
            print('|{}  |'.format(item[0]), end='')
    print()
    for item in list_of_cards:
        print('| {} |'.format(item[1]), end='')
    print()
    for item in list_of_cards:
        if item[0] == 10:
            print('|_10|', end='')
        else:
            print('|__{}|'.format(item[0]), end='')
    print()
    print()


def main():
    # Set up user's bank balance
    bank = 5000

    # Run a hand
    input('Press enter to start the game... ')
    while True:
        # Get bet value
        print('Your balance is ${}'.format(bank))
        print()
        print('How much would you like to bet? ')
        while True:
            bet = input('> $')
            if bet.isdecimal() and int(bet) <= bank:
                bet = int(bet)
                double_available = bank - (bet * 2)
                break  
            print('Invalid bet amount')
        print()
        
        # Run a game     
        outcome = hand(double_available)
        double_multiplier = 1 # default if no double used
        if outcome[1] == 'd': # return value if user 'doubles'
            double_multiplier = 2

        # Check outcome of game and update bank balance, P = player win, D = dealer win, T. = tie s/d = single/double
        if outcome[0] == 'D':
            print('You lost')
            bank -= bet * double_multiplier
        elif outcome[0] == 'P':
            print('You won')
            bank += bet * double_multiplier
        elif outcome[0] == 'T':
            print('It\'s a tie')
        print()
        if bank <= 0:
            print('You have no money left! Thanks for playing')
            return
        else:
            print('Play again? y/n')
            repeat = input('> ')
            if repeat.lower() == 'n':
                print('Thanks for playing')
                return


def hand(double_available):  # Simulates a single round of the game and returns the winner
    # Generate a deck of cards
    deck = []
    for i in range(len(SUITE)):
        for j in range(len(CARD_NO)):
            deck.append([CARD_NO[j], SUITE[i]])
            random.shuffle(deck)

    # Generate initial dealer and user hand
    dealer = [['#', '#'], deck.pop()]
    player = [deck.pop(), deck.pop()]

    print('DEALER: ???')
    show_cards(dealer)

    p_score = score_check(player)
    print('PLAYER: {}'.format(p_score))
    show_cards(player)

    dealer[0] = deck.pop()

    # Check if player has 21 from initial deal
    d_score = score_check(dealer)
    p_score = score_check(player)
    if p_score == 21 and d_score != 21:
        return 'P'
    if p_score == 21 and d_score == 21:
        return 'T'

    while True: # Run a game
        if len(player) == 2 and double_available >= 0: # Ask player what they want to do
            print('(H)it, (S)tick, (D)ouble down?')
            choices = ['h', 's', 'd']
        else: 
            print('(H)it or (S)tick?')
            choices = ['h', 's']
        while True: 
            turn = input('> ')
            if turn.lower() in choices:
                turn = turn.lower()
                break
        print()

        if turn == 's' or turn == 'd': # Player 'sticks' or 'doubles'
            if turn == 'd':
                player.append(deck.pop())
                print('You drew a {} of {}'.format(player[-1][0], player[-1][1]))

            d_score = score_check(dealer)
            p_score = score_check(player)

            while d_score < p_score and d_score < 17 and p_score < 22: # Dealer decides what to do
                dealer.append(deck.pop())
                print('The dealer drew a {} of {}'.format(dealer[-1][0], dealer[-1][1]))
                d_score = score_check(dealer)

            print('DEALER: {}'.format(d_score))
            show_cards(dealer)

            print('PLAYER: {}'.format(p_score))
            show_cards(player)  

            double_check = 's'
            if turn == 'd':
                double_check = 'd'

            if (p_score == 21 and d_score != 21) or (d_score > 21 and p_score < 21):
                return 'P{}'.format(double_check)
            elif d_score == 21 or (p_score > 21 and d_score < 21):
                return 'D{}'.format(double_check)
            elif p_score > d_score:
                return 'P{}'.format(double_check)
            elif d_score > p_score:
                return 'D{}'.format(double_check)
            else:
                return 'T.'
            
        elif turn == 'h': # Player 'hits' - asks for another card 
            player.append(deck.pop())
            print('You drew a {} of {}'.format(player[-1][0], player[-1][1]))

            d_score = score_check(dealer)
            p_score = score_check(player)

            if p_score > d_score and d_score < 17 and p_score < 22: # Dealer decides whether to draw another card
                dealer.append(deck.pop())
                print('The dealer drew a {} of {}'.format(dealer[-1][0], dealer[-1][1]))
                d_score = score_check(dealer)

            print('DEALER: {}'.format(d_score))
            show_cards(dealer)

            print('PLAYER: {}'.format(p_score))
            show_cards(player)

            if (p_score == 21 and d_score != 21) or (d_score > 21 and p_score < 21):
                return 'Ps'
            elif d_score == 21 or (p_score > 21 and d_score < 21):
                return 'Ds'
            elif d_score > 21 and p_score > 21:
                return 'T.'


def score_check(cards):   # A function to check the score of a group of cards
    score = 0
    ace_count = 0

    for i in range(len(cards)):
        if cards[i][0] == 'A':
            score += 11
            ace_count += 1
        elif cards[i][0] in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
            score += cards[i][0]
        elif cards[i][0] in ['J', 'K', 'Q']:
            score += 10

    # Adjust the value of aces which can be either 11 (above) or 1 (below)
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1

    return score


if __name__ == '__main__':
    main()