# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:42:18 2019

@author: rounak
"""

num = int (input("Enter a number: "))

#if the elements in the range(2, num) evenly divides the num,
#then it is included in the divisors list
divisor = [x for x in range(2, num) if num % x == 0]

for x in divisor:
    print(x)
