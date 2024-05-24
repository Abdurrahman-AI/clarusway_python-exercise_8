# -*- coding: utf-8 -*-
"""
Created on Fri May 24 21:20:53 2024

@author: HP
"""

# Ex_3_2_ Add a function that takes a string and returns True if the string 
# is a pangram(contains all of the letters of the alphabet) and returns 
# False if the string is not a pangram.

def is_pangram(s):
    s = s.lower()     # Converting the string to lowercase to handle both uppercase and lowercase letters
    
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')   #creating a set of all the letters 
    
    string_set = set(s)   # creating a set of all the letters in the string
    
    return alphabet_set.issubset(string_set)  

# Example usage
example_string1 = "Badec gifhjk lompn turqus vwxyz"
example_string2 = "Hello world"


print(f'Is the string "{example_string1}" a pangram? {is_pangram(example_string1)}')
print(f'Is the string "{example_string2}" a pangram? {is_pangram(example_string2)}')
