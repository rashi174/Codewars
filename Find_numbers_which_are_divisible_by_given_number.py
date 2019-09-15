"""Description:
Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. First argument is an array of numbers and the second is the divisor.

Example
divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]
"""

#Clever Approach

def divisible_by(numbers, divisor):
    return [x for x in numbers if x%divisor == 0]


"""
##My approach


def divisible_by(numbers, divisor): 
    list2=[]
    for item in numbers:
        if item%divisor==0:
            list2.append(item)
    return list2
"""