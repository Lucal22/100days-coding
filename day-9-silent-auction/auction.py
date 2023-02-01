
all_bets = {}


def set_bet(name, bet):
    all_bets[name] = bet


def new_bet():
    new_bet = input('Is that any other bet?(yes/no)\n')
    if new_bet == 'yes':
        bet()

    highest_bid = 0
    winner = ''

    if new_bet == 'no':

        for bidder in all_bets:
            bid_amount = all_bets[bidder]

            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bidder

        print(f'The winner is {winner}')


def bet():
    name = input('Whats your name?\n')
    bet = int(input('How much you wanna bid?\n'))
    set_bet(name, bet)
    new_bet()


bet()

# print(all_bets)
