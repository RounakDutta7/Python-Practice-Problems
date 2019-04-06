# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:10:20 2019

@author: rounak
"""

input_list = input("Enter a list of numbers: ")
list = input_list.split() #separting the elements by spaces in the list

for x in list:
    if int(x) < 5:
        print(x)
        
print([x for x in list if int(x) < 5 ])

num = int( input("Enter a number: "))
print([x for x in list if int(x) < num ])
