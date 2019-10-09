"""

Description:
For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.

In C: do not dynamically allocate memory,
      instead return a string leteral
      
     """

def well(x):
    if x.count("good") == 0:
        return "Fail!"
    elif x.count("good") <= 2:
        return "Publish!"
    else:
        return "I smell a series!"
    
    
    
"""

def well(x):
    c = x.count('good')
    return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'
    
    """