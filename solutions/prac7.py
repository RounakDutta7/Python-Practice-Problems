# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:49:02 2019

@author: rounak
"""

input_str = input("Enter a list of elements: ")

list1 = [int(x) for x in input_str.split() if int(x) % 2 == 0]

print(list1)