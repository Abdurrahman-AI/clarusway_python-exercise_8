# -*- coding: utf-8 -*-
"""
Created on Fri May 24 19:53:22 2024

@author: HP
"""
# Ex.8.1.1. Write a program that contains a function that gets the sum of all 
#  numbers in a list. Don’t use the built in sum() function.


def get_sum(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum

numbers = [1, 3, 5, 7, 9]
sum_of_numbers = get_sum(numbers)
print('The sum of the numbers in the list is:', sum_of_numbers)