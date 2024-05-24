# -*- coding: utf-8 -*-
"""
Created on Fri May 24 22:04:14 2024

@author: HP
"""

# Ex_8_5
# An Armstrong number is the number in any given number base, which forms 
# the total of the same number, when each of its digits is raised to the 
# power of the number of digits in the number. There are no 2 digit armstrong 
# numbers. For more clarification look up Armstrong numbers on google.

# Write a program that takes a number from the user and gives all of the
# armstrong numbers from 0 to that number. Create at least one function.

def is_armstrong_number(num):
  """Checks if a number is an Armstrong number."""
  num_str = str(num)     # checking if a number is an Armstrong number.
  digits = len(num_str)
  sum_of_powers = 0
  for digit in num_str:
    sum_of_powers += int(digit) ** digits
  return sum_of_powers == num

def find_armstrong_numbers(upper_limit):
  armstrong_numbers = []      # finding Armstrong numbers from 0 to the upper limit
  for num in range(upper_limit + 1):
    if is_armstrong_number(num):
      armstrong_numbers.append(num)
  return armstrong_numbers

# Entering user input with validation
while True:
  upper_limit_str = input("Enter an upper limit (positive integer): ")
  if upper_limit_str.isdigit() and int(upper_limit_str) >= 0:
    upper_limit = int(upper_limit_str)
    break
  else:
    print("Please enter a non-negative integer.")

# Listing Armstrong numbers
armstrong_list = find_armstrong_numbers(upper_limit)

if armstrong_list:
  print("Armstrong numbers from 0 to", upper_limit, "are:", armstrong_list)
else:
  print("No Armstrong numbers found in the range 0 to", upper_limit)