'''a program to check palindrome number.'''


userInput = input("give me a Number: ")

def palindrome(num):
    #num is palindrome check cheyyanm 121 == 121 
    lenn = len(num)
    for i in range(lenn):
        if num[i] != num[lenn-i-1]:
            print("its not a palindrome")
            return
    print("its a palindrome")
    
# def palindrome(num):
#     rever = num[::-1]
#     if int(num)==int(rever):
#         print("Number is Palindrome")
#     else:
#         print("Number is not palindrome")

palindrome(userInput)





      



        