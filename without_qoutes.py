"""
Description:
Task
You need to create a function, helloWorld, that will return the String Hello, World! without actually using raw strings. This includes quotes, double quotes and template strings. You can, however, use the String constructor and any related functions.

You cannot use the following:

"Hello, World!"
'Hello, World!'
`Hello, World!`

"""


#Clever approach

"""
hello_world=lambda:bytes([72,101,108,108,111,44,32,87,111,114,108,100,33]).decode()

"""


#my_approach
"""

def hello_world():
  return chr(72) + chr(101) + chr(108) + chr(108) + chr(111) + chr(44) + chr(32) + chr(87) + chr(111) + chr(114) + chr(108) + chr(100) + chr(33)
"""