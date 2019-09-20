"""

Codewars 6:Kyu
Description:
Write a function that takes an integer as input,
and returns the number of bits that are equal to one in the binary 
representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, 
so the function should return 5 in this case
"""

def countBits(n):
    c=0
    x=bin(n)[2:]
    x=list(x)
    for i in x:
        if i=='1':
            c=c+1
    return c
    
    
    
    
##Clever approach
    
def countBit(n):
    return bin(n).count("1")
    
    
    
    
    