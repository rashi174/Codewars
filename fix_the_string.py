def solve(string):
    count1=0
    count2=0
    for i in string:
        if(i.islower()):
            count1=count1+1
        elif(i.isupper()):
            count2=count2+1
    if count1>count2:
        return string.lower()
    elif count1<count2:
        return string.upper()
    else:
        return string.lower()
  