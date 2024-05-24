# -*- coding: utf-8 -*-
"""
Created on Fri May 24 19:56:16 2024

@author: HP
"""
# Ex_8_1_2_Now add a function that takes a list and removes 
# all of the duplicates from that list. Hint: You can use sets.

def get_sum(numbers):
  total_sum = 0
  for num in numbers:
    total_sum += num
  return total_sum

def remove_duplicates(numbers):
  
  unique_numbers = set(numbers)  # Converting list to set to remove duplicates
  return list(unique_numbers)    # Converting set back to list

# Sample list 
numbers = [1, 2, 5, 8, 3, 2, 1]

# The sum using the get_sum function
sum_of_numbers = get_sum(numbers)

unique_list = remove_duplicates(numbers.copy())  

print("The sum of the numbers in the list is:", sum_of_numbers)
print("The list with duplicates removed:", unique_list)