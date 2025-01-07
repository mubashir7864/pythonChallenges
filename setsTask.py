'''a Python program that takes a string as input and checks if all the
characters in the string are unique (i.e., no character repeats). Return True if all
characters are unique, and False otherwise'''
userInput = input("give me a Word: ")
def uniqueString(inp):
    inp =inp.lower()
    string1 = len(inp.replace(" ",""))  #if user give a space 2 times then output will be false, when also the string is unique
    uniq = set(inp.replace(" ",""))

    if len(uniq) == string1:
        return True
    else:
        return False

print(uniqueString(userInput))