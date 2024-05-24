# -*- coding: utf-8 -*-
"""
Created on Fri May 24 20:37:28 2024

@author: HP
"""

# Ex_8_2_Write a program that contains a function that takes two integers 
# and creates a list with all numbers between the first and second integer.

def get_numbers_between(start, end):
  numbers = []
  for num in range(start, end + 1):
    numbers.append(num)
  return numbers

# Example 
start_num = 4
end_num = 8
list_of_numbers = get_numbers_between(start_num, end_num)

print("List of numbers between", start_num, "and", end_num, ":", list_of_numbers)