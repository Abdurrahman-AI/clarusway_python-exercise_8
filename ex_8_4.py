# -*- coding: utf-8 -*-
"""
Created on Fri May 24 21:56:38 2024

@author: HP
"""
# Ex_8_4
# Write a program that contains a function that takes a letter and 
# returns whether it is a vowel or consonant. Take an input string from 
# the user and write a program that tells the number of vowels and consonants 
# in that string.

def is_vowel(char):
  vowels = 'aeiouAEIOU'
  return char in vowels

def count_vowels_consonants(text):
  vowel_count = 0
  consonant_count = 0
  for char in text:
    if char.isalpha():  # Check if character is a letter
      if is_vowel(char):
        vowel_count += 1
      else:
        consonant_count += 1
  return vowel_count, consonant_count

# Entering an user input
user_text = input("Enter a string: ")

# Counting vowels and consonants
vowels, consonants = count_vowels_consonants(user_text)

print("Vowels:", vowels)
print("Consonants:", consonants)