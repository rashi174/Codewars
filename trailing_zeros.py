def zeros(n):
    ret = 0
    i = 5
    
    while n / i >= 1:
        ret += n // i
        i *= 5
    
    return ret



"""Clever solution


def zeros(n):
  x = n/5
  return x+zeros(x) if x else 0
  
  
  """