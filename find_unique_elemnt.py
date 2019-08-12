
"""Using set"""

def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

"""naive method

def find_uniq(arr):
    # your code here
    arr.sort()

    if(arr[0] < arr[-1] and arr[0] < arr[-2]):
        n = arr[0]
    else:
        n = arr[-1]


    return n   # n: unique integer in the array
"""