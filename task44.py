#Write a Python program to find numbers divisible by nineteen or thirteen from a list
# of numbers using Lambda.


listNum = [45,56,89,78,19,63,98.13,45,253,468]


divisible = list(filter(lambda num: num % 19 == 0 or num % 13 == 0, listNum))


print("Numbers divisible by 19 or 13:", divisible)
    

