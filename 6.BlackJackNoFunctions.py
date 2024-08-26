from art import logo
import random

deck = [2,3,4,5,6,7,8,9,10,11]
begin_game = True
player_score=0
computer_score= 0
player_bust= False
computer_bust= False
computer_cards=[]
player_cards=[]

print(logo)
play_more = input("Do you want to play a game o Blackjack? Type 'y' or 'n': ")

while begin_game:
    if play_more == "n":
        begin_game = False
    else:
        computer_cards.append(random.randint(2, 11))
        print("\n"*20)
        print(logo)
        for j in range(0, 2):
            player_cards.append(random.randint(2, 11))
        player_score = 0
        for c in player_cards:
            player_score += c
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        hit_ = input("Type 'y' to get another card, type 'n' to pass: ")
        while hit_ == "y" and player_score <= 21:
            print("\n" * 20)
            print(logo)
            player_cards.append(random.randint(2, len(deck)))
            player_score = 0

            for i in player_cards:
                player_score += i

                if player_score > 21:
                    temp1 = -1
                    for a in player_cards:
                        temp1 += 1
                        if a == 11 and player_score > 21:
                            player_cards[temp1] = 1
                            player_score = 0
            player_score = 0
            for j in player_cards:
                player_score += j
            if player_score <= 21:
                print(f"Your cards: {player_cards}, current score: {player_score}")
                print(f"Computer's first card: {computer_cards[0]}")
                hit_ = input("Type 'y' to get another card, type 'n' to pass: ")
            else:
                hit_ = "n"
                player_bust = True

        print("\n" * 20)
        print(logo)
        if player_bust:
            print("Woops, looks like you are busted!")
            print(f"Your final hand: {player_cards}, final score: {player_score}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
            print("You lose!!")
        else:
            computer_cards = []
            computer_score = 0
            computer_cards.append(random.randint(2, 11))
            for c in computer_cards:
                computer_score += c

            test1 = True
            while test1:

                if computer_score < 17:
                    computer_score = 0
                    computer_cards.append(random.randint(2, 11))
                    for c in computer_cards:
                        computer_score += c

                if computer_score < player_score:
                    computer_score = 0
                    computer_cards.append(random.randint(2, 11))
                    for c in computer_cards:
                        computer_score += c
                else:
                    test1 = False

                if computer_score > 21:
                    temp2 = -1
                    for a in computer_cards:
                        temp2 += 1
                        if a == 11 and computer_score > 21:
                            computer_cards[temp2] = 1
                            computer_score = 0

                computer_score = 0
                for j in computer_cards:
                    computer_score += j

                if computer_score > 21:
                    computer_bust = True
                    test1 = False
            if computer_bust:
                print("Computer is busted!")
                print(f"Your final hand: {player_cards}, final score: {player_score}")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("You win!!")
            else:
                if player_score > computer_score:
                    print(f"Your final hand: {player_cards}, final score: {player_score}")
                    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                    print("You win!!")
                elif player_score == computer_score:
                    print(f"Your final hand: {player_cards}, final score: {player_score}")
                    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                    print("Bet is returned!!")
                else:
                    print(f"Your final hand: {player_cards}, final score: {player_score}")
                    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                    print("You lose!!")

    play_more = input("Do you want to play a game o Blackjack? Type 'y' or 'n': ")