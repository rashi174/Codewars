# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 00:14:30 2019
Description:
It's pretty straightforward. Your goal is to create a function that removes the first 
and last characters of a string. You're given one parameter, the original string. 
You don't have to worry with strings with less than two characters.
@author: Rashi
"""


def remove_char(s):
    return s[1 : -1]