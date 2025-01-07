userInput = input("what number table You Need? ")

for i in range(1,11):
    num = int(userInput)
    print(f"{num} * {i} = {num*i}",end="")
    print()
    
