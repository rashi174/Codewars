"""
https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/train/python

Challenge:

Given a two-dimensional array of integers, return the flattened version of the array 
with all the integers in the sorted (ascending) order.

Example:

Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], 

your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].

#### 7 kyu  ####

"""




def flatten_and_sort(array):
    s=[]
    for item in array:
          s=s+item
    return sorted(s)
   
    


#Best practice
    

from itertools import chain
def flaten_and_sort(array):
    return sorted((chain(*array)))
