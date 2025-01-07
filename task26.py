'''a Python program that uses a list comprehension to create a new list that
contains only the uppercase letters in an existing list of strings'''

oldList = ["A","d","k","p","L","m","U","f","I"]

newList = [i for i in oldList if i == i.upper()]

print(newList)