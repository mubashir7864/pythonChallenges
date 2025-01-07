"find the number is prime or not"

userInput= int(input("enter a Number: "))


def primeNumber(num):
    count = 0
    for i in range(1,num+1):
        if (num%i == 0):
            count += 1
    if count == 2:
        print("its a prime Number")
    else:
        print("its not a prime number")

primeNumber(userInput)
        

