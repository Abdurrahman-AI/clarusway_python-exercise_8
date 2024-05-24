# -*- coding: utf-8 -*-
"""
Created on Fri May 24 20:44:06 2024

@author: HP
"""

# Ex_8_3_1_Write a program that contains a function that takes a letter and 
# checks which number of the alphabet that letter is. So the letter: ‘a’ will
# be 1, The letter: ‘b’ will be 2 etc.

def get_letter_position(letter):
  alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
  alphabet_upper = alphabet_lower.upper()
  if letter.isalpha():
    if letter.islower():
      return alphabet_lower.index(letter) + 1
    else:
      return alphabet_upper.index(letter) + 1
  else:
    return "Input must be a letter."

# Example usage with lowercase and uppercase letters
letters = ['a', 'Z', '!']
for letter in letters:
  position = get_letter_position(letter)
  print(f"The position of '{letter}' is: {position}")