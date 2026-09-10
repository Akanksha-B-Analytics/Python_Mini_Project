# Caesar Cipher Program
# A text encryption and decryption tool built with Python.
# Users can encode and decode messages using a shift-based
# cipher while preserving spaces and special characters.
# This project demonstrates functions, loops, conditionals,
# string manipulation, and basic cryptography concepts.


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        
        if letter not in alphabet:
            output_text += letter
        else:
          shifted_position = alphabet.index(letter) + shift_amount
          shifted_position %= len(alphabet)
          output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

start = True
while start :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction) ##calling the defined funtion
    restart=input("Do you want to restart 'yes'or 'no'?\n").lower()
    if restart == "no":
        start = False
        print("Goodbye!")


