# Write a Python program to check that a string contains only a certain set of
# characters (in this case a-z, A-Z and 0-9)

import re

namestring = "muhagsh@.."

nameString2 = "Mubashir78"

def matchstring(string):
    if re.match('^[a-zA-Z0-9 ]*$',string):
        return True
    else:
        return False

print(matchstring(namestring))
print(matchstring(nameString2))