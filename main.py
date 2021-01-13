import random
from replit import clear
from art import logo


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)


    return sum(cards)


def compare(user_hand, computer_hand):
    if user_hand == computer_hand:
        return "It's a draw"
    elif computer_hand == 0:
        return "You lose, opponent has Blackjack"
    elif user_hand == 0:
        return "You Win with Blackjack!"
    elif user_hand > 21:
        return "You went over, you lose..."
    elif computer_hand > 21:
        return "Opponent went over, you win!"
    elif user_hand > computer_hand:
        return "You Win!"
    else:
        return "You lose..."


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, User score: {user_score}")
        print(f"Computer cards: {computer_cards[0]}, Computer score: uknown")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            play = input("Type 'y' to hit, type 'n' to pass: ")
            if play == 'y':
                user_cards.append(deal_card())
                calculate_score(user_cards)
                if user_score == 0 or computer_score == 0 or user_score > 21:
                    is_game_over = True
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    print(logo)
    play_game()
