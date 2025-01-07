'''write a program in python find the second smallest and third largest number
in a list.'''

listnumbers = [12,45,78,65,32,59,4,2,55,68,9]

listnumbers.sort()

print(f"the second smallest number in list is: {listnumbers[1]} \n The Third largest Number in list is: {listnumbers[len(listnumbers)-3]}")



