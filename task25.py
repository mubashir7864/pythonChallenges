'''a Python program that uses a "for" loop to iterate over a string and prints
out each character along with its count.'''

userInput = input("enter a string: ")
newDict = {}

for i in userInput:
    if i not in newDict.keys():
        newDict[i] = 1
    else:
        newDict[i] += 1

print(newDict.items())


    




