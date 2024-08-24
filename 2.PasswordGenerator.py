import random
from itertools import repeat

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
sum_of_char= nr_numbers + nr_symbols + nr_letters
if sum_of_char < 6:
    print("Your password must contain at least six(6) characters. Please try again!")
else:
    password = ""
    nr_let_lim = 0
    nr_sym_lim = 0
    nr_num_lim = 0
    pass_let= []
    pass_num= []
    pass_sym= []
    a = 0
    b = 0
    c = 0

    if nr_letters > 0:
        for loopz in range(0, nr_letters):
            ran_let_char = letters[random.randint(0,len(letters)-1)]
            pass_let.append(ran_let_char)
    if nr_symbols > 0:
        for loopz in range(0, nr_symbols):
            ran_sym_char = symbols[random.randint(0, len(symbols)-1)]
            pass_sym.append(ran_sym_char)
    if nr_numbers > 0:
        for loopz in range(0, nr_numbers):
            ran_num_char = numbers[random.randint(0, len(numbers)-1)]
            pass_num.append(ran_num_char)

    while len(password) != sum_of_char:
        choice_of_lists = random.randint(0, 2)
        if choice_of_lists == 0 and nr_let_lim < nr_letters:
            nr_let_lim += 1
            password += pass_let[a]
            a+= 1
        elif choice_of_lists == 1 and nr_sym_lim < nr_symbols:
            nr_sym_lim += 1
            password += pass_sym[b]
            b+= 1
        elif choice_of_lists == 2 and nr_num_lim < nr_numbers:
            nr_num_lim += 1
            password += pass_num[c]
            c+= 1
    print(password)


