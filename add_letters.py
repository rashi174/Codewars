"""
Description:
Your task is to add up letters to one letter.

The function will be given a variable amount of arguments, each one being a letter to add.

Notes:
Letters will always be lowercase.
Letters can overflow (see second to last example of the description)
If no letters are given, the function should return 'z'
Examples:
add_letters('a', 'b', 'c') = 'f'
add_letters('a', 'b') = 'c'
add_letters('z') = 'z'
add_letters('z', 'a') = 'a'
add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
add_letters() = 'z'
Confused? Roll your mouse/tap over here

ALGORITHMS
Suggest kata description edits

"""

def add_letters(*letters):
    #97 == 'a' and 122 = 'z'
    alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    sum = 0
    for i in letters:
        sum += alpha_list.index(i)+1
    
    while sum > 26:
        sum -= 26
    
    return alpha_list[sum-1]