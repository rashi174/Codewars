
"""Description:
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

each taken only once - coming from s1 or s2.
Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""


"""
##Clever Approach

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))
"""


##My Approach

def longest(s1, s2):
    s3=s1+s2
    str1=""
    result=sorted(set(s3))
    return str1.join(result)
    