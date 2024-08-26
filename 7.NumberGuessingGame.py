import random
numbers_list = []
for i in range(0,101):
    numbers_list.append(i)

print(numbers_list)
print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100.")

correct_number = random.choice(numbers_list)
print(f"haha its {correct_number}")
game_ = True
mode_ = input("Choose a difficulty. Type 'easy' or 'hard': ")

if mode_ == 'easy':
    lives_ = 10
else:
    lives_= 5

print(f"You have {lives_} attempts remaining to guess the number")
while game_:
    guess_ = int(input("Make a guess: "))
    if lives_>0:
        if guess_ > correct_number:
            print("Too high.")
            print("Guess again.")
            lives_ -= 1
            print(f"You have {lives_} attempts remaining to guess the number")
        elif guess_< correct_number:
            print("Too low.")
            print("Guess again.")
            lives_ -= 1
            print(f"You have {lives_} attempts remaining to guess the number")
        elif guess_ == correct_number:
            print("Correct!!")
            game_ = False
    else:
        game_= False
