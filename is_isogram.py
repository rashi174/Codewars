"""  
    
t=input()
w=set(t)
if(len(t)==len(w)):
    print("Yes")
else:
    print("No")
"""


def is_isogram(string):
    return len(string) == len(set(string.lower()))