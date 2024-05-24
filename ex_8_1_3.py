# -*- coding: utf-8 -*-
"""
Created on Fri May 24 20:22:24 2024

@author: HP
"""

# Ex_8_1_3_ Create the following list: [1, 2, 3, 4, 4, 3, 2, 1]. 
# Now print the sum of all of the numbers in that list, excluding 
# the duplicates using only one line of code and the functions you made.

def get_sum(numbers):
  total_sum = 0
  for num in numbers:
    total_sum += num
  return total_sum

def remove_duplicates(numbers):
  unique_numbers = set(numbers)
  return list(unique_numbers)

# Sample list with duplicates
numbers = [1, 2, 3, 4, 4, 3, 2, 1]

sum_without_duplicates = get_sum(remove_duplicates(numbers))

print("The sum of the unique numbers in the list is:", sum_without_duplicates)