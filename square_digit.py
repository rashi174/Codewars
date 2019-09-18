"""
Description:

    Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer

"""



##My Approach
def square_digits(num):
    list1=[]
    num=str(num)
    for item in num:
        item=int(item)
        x=item*item
        list1.append(x)
    res = int("".join(map(str, list1)))
    return res


##Clever approach
def square_digit(num):
    return int(''.join(str(int(d)**2) for d in str(num)))