# Write a Python program that matches a string that has an a followed by zero or
# one 'b'


import re

namestring = "abhagsh@.."

nameString2 = "Mubashir78"

def matchstring(string):
    if re.match(r'^a[b]?',string):
        return True
    else:
        return False

print(matchstring(namestring))
print(matchstring(nameString2))