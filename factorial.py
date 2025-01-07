userInput=input(("enter a number: "))
# 5**4*3**2*1
userInput = int(userInput)
factorial = 1

for i in range(userInput,1,-1):
    factorial *= i

print(factorial)
    


