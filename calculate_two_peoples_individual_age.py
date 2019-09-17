"""
Description:
Create a function that takes in the sum and age difference of two people, calculates their individual ages, and returns a pair of values if those exist or an empty values if:

sum < 0
difference < 0
Either of the calculated ages come out to be negative
"""


#My Approach

def get_ages(sum_, difference):
    x=sum_+difference
    x=x/2
    y=sum_-x
    if sum_<0 or difference<0 or x<0 or y<0:
        return None
    else: 
        return x,y
    
"""
#Clever approach

def get_ages(a,b):
    x = (a+b)/2
    y = (a-b)/2
    return None if a<0 or b<0 or x<0 or y<0 else (x,y)
    
    
"""