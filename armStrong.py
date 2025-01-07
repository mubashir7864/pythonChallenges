'''a program to check Armstrong number'''

userInput = input("give me a Number: ")
inputLen = len(userInput)


def armStrong(num):
    sum = 0
    for i in num:
        sum += pow(int(i),inputLen)
    if sum == int(num):
        print("This is a Armstrong Number")
    else:
        print("this is not a armstrong number")

armStrong(userInput)
