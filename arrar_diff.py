def array_diff(a, b):
    for i in b:
        if i in a:
            while i in a:
                a.remove(i)
    return a







####Best approaches:



"""


def array_diff(a, b):
    return [x for x in a if x not in b]
    
"""


"""def array_diff(a, b):
    #your code here
    return filter(lambda i: i not in b, a)
"""



"""    
    
def array_diff(a, b):
    #your code here
    a=list(a)
    b=list(b)
    for item in b:
        if item in a:
            a.remove(item)
    return a
"""