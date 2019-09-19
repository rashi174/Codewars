
"""Description:
This method, which is supposed to return the result of dividing its first argument by its second, 
isn't always returning correct values. Fix it.
"""


def divide_numbers(x,y):
    return x/y

#NOTE: I just switched the Python Version to 3.6 
#where Python no longer truncates integer division
    
def divide_number(x,y):
    return float(x) / float(y)