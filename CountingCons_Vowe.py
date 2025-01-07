
# Take user Input
userInput = input("Enter a WORD sO I will help you count Vowels and Consonents in it: ")

output = {"Vowels": 0 , "Consonents ": 0}

# Checks userInput  through Loop
for chr in userInput.lower():
    vowels = ["a","e","i","o","u"]
    if chr in vowels:
        output["Vowels"] += 1
    else:
        output["Consonents "] += 1

#Print Output 
print(f"For {userInput} Word Contains = ",output)

