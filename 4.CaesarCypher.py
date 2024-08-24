# TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(encode_or_decode,original_text,shift_amount):
    cipher_text = ""
    if encode_or_decode == "encode":
        cipher_text=""
        for i in original_text:
            if i not in alphabet:
                cipher_text+= i
            elif alphabet.index(i)+int(shift_amount) > 25:
                cipher_text+=alphabet[alphabet.index(i) + int(shift_amount) - 26]
            else:
                cipher_text+=alphabet[alphabet.index(i)+int(shift_amount)]
    elif encode_or_decode == "decode":
        for i in original_text:
            if i not in alphabet:
                cipher_text += i
            elif alphabet.index(i) - int(shift_amount) < 0:
                cipher_text += alphabet[alphabet.index(i) - int(shift_amount) + 26]
            else:
                cipher_text += alphabet[alphabet.index(i) - int(shift_amount)]
    print(f"Here is the result: {cipher_text}")


# TODO-3: Can you figure out a way to restart the cipher program?

over = True
while over:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart_ = input("Would you like to restart if yes press: yes. If not press: no\n")
    if restart_ == "no":
        over= False




