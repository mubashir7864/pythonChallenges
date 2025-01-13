
# Take user Input
userInput = input("Enter a WORD sO I will help you count Vowels and Consonents in it: ")

def vowels(strb):
    newdict = {"vowels":0,"consonant":0}
    for i in strb.lower():
        if i in ["a","e","i","o","u"]:
            newdict["vowels"] += 1
        else:
            newdict["consonant"] += 1
    return newdict

print(vowels(userInput))

