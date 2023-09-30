# The Caesar Cipher, used by Julius Caesar around 58 BC, is a substitution cipher that shifts letters in a message to make it unreadable if intercepted. 

# This program is a computerized version of the same.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Prompting user for inputs
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Functions for encoding and decoding the message based on the number of shifts.
def encrypt(input_message, shifts):
  message = ""
  for letter in input_message:
    position = alphabet.index(letter)
    new_position = position+shifts
    if new_position>25:
      extend = new_position-26
      new_letter = alphabet[extend]
    else:
      new_letter = alphabet[new_position]
    message+=new_letter
  print(f"Encoded message is: {message}")

def decrypt(input_text, set_shifts):
  decryted_text = ""
  for letter in input_text:
    position = alphabet.index(letter)
    new_position = position - set_shifts
    if new_position<0:
      extend = new_position+26
      new_letter = alphabet[extend]
    else:
      new_letter = alphabet[new_position]
    decryted_text += new_letter
  print(f"Decoded message is: {decryted_text}")

if direction.lower() == 'encode':
  encrypt(input_message=text,shifts=shift)

if direction.lower() == 'decode':
  decrypt(input_text=text, set_shifts=shift)
