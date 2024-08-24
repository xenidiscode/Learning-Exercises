rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
hand_gestures_int = random.randint(0, 2)
hand_gestures_str = [rock, paper, scissors]

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
player_choice = int(player_choice)
print(hand_gestures_str[player_choice])
computer_choice = hand_gestures_str[hand_gestures_int]
print("Computer Chose: ")
print(computer_choice)

if player_choice == 0:
    if hand_gestures_int == 0:
        print("Its a Tie")
    elif hand_gestures_int == 1:
        print("You lose")
    else:
        print("You win")
elif player_choice == 1:
    if hand_gestures_int == 0:
        print("You Win")
    elif hand_gestures_int == 1:
        print("Its a Tie")
    else:
        print("You lose")
else:
    if hand_gestures_int == 0:
        print("You lose")
    elif hand_gestures_int == 1:
        print("You win")
    else:
        print("Its a Tie")
