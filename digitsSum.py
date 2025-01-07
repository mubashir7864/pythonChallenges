''' a program to print sum of digits'''

userInput = input("give me a Number: ")

def digitsSum(num):
    sum = 0
    for i in num:
        sum += int(i)
    return sum


print(digitsSum(userInput))


