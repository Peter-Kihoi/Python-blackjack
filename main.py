import random


def add_card(player, card):
    for i in range(0, 2):
        player.append(random.choice(card))


def check_blackjack(player):
    if 10 in player and 11 in player:
        return True
    return False


def total(player):
    player_total = sum(player)
    return player_total


def over_and_ace(player_total, player):
    if player_total > 21 and 11 in player:
        player_total -= 10
        return player_total
    else:
        return player_total


def check_win(computers, users):
    if users == computers:
        print("draw")
    elif users > 21:
        print("You went over. you loose")
        return
    elif computers > 21:
        print("computer went over. you win")
    elif users > computers:
        print("you win")
    else:
        print("you loose")


def blackjack():
    game_on = True
    while game_on:
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play == 'n':
            return

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        user = []
        computer = []
        add_card(user, cards)
        add_card(computer, cards)
        comp_total = total(computer)
        user_total = total(user)
        user_total = over_and_ace(user_total, user)
        comp_total = over_and_ace(comp_total, computer)

        if comp_total < 17:
            computer.append(random.choice(cards))
            comp_total = total(computer)
            comp_total = over_and_ace(comp_total, computer)

        print(f"Your cards: {user}, current score: {user_total} ")
        print(f"computer's first card: {computer[0]}")

        if check_blackjack(user):
            print("You win")
        elif check_blackjack(computer):
            print("you loose")
        else:

            pick = True
            while pick:
                if input("Type 'y' to get another card, type 'n' to pass: ") == 'n':

                    print(f"your final hand: {user}, final score: {user_total}")
                    print(f"Computer's final hand: {computer}:, final score: {comp_total}")

                    check_win(comp_total, user_total)
                    pick = False

                else:
                    user.append(random.choice(cards))
                    user_total = total(user)
                    user_total = over_and_ace(user_total, user)

                    if user_total > 21:
                        print(f"your final hand: {user}, final score: {user_total}")
                        print(f"Computer's final hand: {computer}:, final score: {comp_total}")
                        print("You went over. you loose")
                        pick = False
                    elif comp_total > 21:
                        print(f"your final hand: {user}, final score: {user_total}")
                        print(f"Computer's final hand: {computer}:, final score: {comp_total}")
                        print("computer went over. you win")
                        pick = False

                    else:
                        print(f"Your cards: {user}, current score: {user_total} ")
                        print(f"computer's first card: {computer[0]}")


blackjack()
