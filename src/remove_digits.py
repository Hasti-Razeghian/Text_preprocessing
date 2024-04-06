import re

"""Takes a string and remove digits"""

unwanted_digit = ['0','1','2','3','4','5','6','7','8','9']
def remove_digits(data:str):
    for digit in unwanted_digit:
        data = data.replace(digit, "")
    return  data