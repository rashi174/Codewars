##My approach
"""
import string 
  
def ispangram(str): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in str.lower(): 
            return False
  
    return True
"""


###Best /clever approach

import string

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())