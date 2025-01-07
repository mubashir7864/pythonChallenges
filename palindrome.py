# program to check Palindome Example  Noon , level, rotor

# Takes User input
userInput = input("enter a word: ").lower()
userinputreversed = userInput[::-1]

print(userinputreversed)

if userInput == userinputreversed:
    print("its palindrome")
else:
    print("its not a palindrome")




