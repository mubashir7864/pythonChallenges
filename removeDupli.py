# program to remove duplicate values in the given string.

userInput = input("enter a word: ").replace(" ","")

#convertString = set(userInput)
#print(convertString)

convertedString = ""
duplicateChrs = ""

for i in userInput.lower():
    if i not in convertedString:
        convertedString += i 
    else: 
        duplicateChrs += i
print(f"Duplicate removed string: {convertedString}\n Duplicate character are: {duplicateChrs}")