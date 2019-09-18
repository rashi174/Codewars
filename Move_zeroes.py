"""
'''
	5kyu - Moving Zeros To The End
	https://www.codewars.com/kata/moving-zeros-to-the-end/solutions/python
'''
Description:
 
Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.

Example:
    
move_zeros([false,1,0,1,2,0,1,3,"a"]) 
# returns[false,1,1,2,1,3,"a",0,0]

"""




#My Approach
def move_zeros(array):
    
    w = []
    d = 0
    
    for i in array:
        if i is False:
            w.append(False)
        elif i == 0:
            d += 1
        else:
            w.append(i)
    for i in range(0,d):
        w.append(0)
    
    print (w)
    return (w)



#Clever Approach!!
    
def move_zero(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))