# -*- coding: utf-8 -*-
"""
Description:
This kata is about multiplying a given number by eight 
if it is an even number and by nine otherwise.
Created on Sat Sep 14 00:26:06 2019

@author: Rashi
"""
#my approach
def simple_multiplication(number) :
    return number * 9 if number % 2 else number * 8



    """
____________________________________________________________________

##Clever approach

def simple_multiplication(n) :
    return n * (8 + n%2)
    
"""