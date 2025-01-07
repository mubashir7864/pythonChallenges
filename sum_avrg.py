#Write a Python program that takes a list of numbers as input and calculates and
#prints the sum and average of those numbers

userInput = input("give a list of numers : ")
userInput = list(userInput)
length = len(userInput)

sum = 0
avrg = 0

for i in userInput:
    i=int(i)
    sum += i
    
print(f"the Sum of given Numbers : {sum} \nthe Average of given Numbers {sum/length} ")
