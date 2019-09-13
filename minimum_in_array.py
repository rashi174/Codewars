# -*- coding: utf-8 -*-
"""Description:
Given an array of integers your solution should find the smallest integer.

For example:

Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, that the supplied array will not be empty.
Created on Fri Sep 13 23:29:01 2019

@author: Rashi
"""
#My Approach
def find_smallest_int(arr):
  return sorted(arr)[0]

##Clever Approach

def findSmallestInt(arr):
    return min(arr)  #the min function finds the minimum value in a list