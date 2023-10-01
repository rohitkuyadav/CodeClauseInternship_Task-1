"""
Made by   : Rohit Kumar Yadav
Created On: 01 Oct 2023
"""

import random   # Generate random integers,stings,floats
import string   #The string module is a built-in Python module that provides
                #various string-related constants, functions, and classes

length = int(input("Password Length: "))
chars = string.ascii_letters   # this function return all the characters from(a-z)lower and upper case both
nums= string.digits            # this function return digits i.e(1234567890)
symbols = string.punctuation   # this function return all the possible symbols i.e(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)

combination = chars+nums + symbols  # combine all the possible combinations
password = ""
for main in range(length):
    password+="".join(random.choice(combination))

print(f"\nOutput Password: %s" % password)
    