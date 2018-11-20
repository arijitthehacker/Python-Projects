#!/bin/python3
# This is a basic implementation of Caesaer Cipher

alphabet = 'abcdefghijklmnopqrstuvwxyz'

message = input("Enter your message: ")
key = input("Enter your key (1-26): ") # String Datatype
key = int(key) # Converted to int

new_message = ''

for each_char in message:
  position = alphabet.find(each_char)
  new_position = (position+key) % 26
  new_character = alphabet[new_position]
  new_message += new_character

print(new_message)
