# Write a Python program to square and cube every number in a given list of integers
# using Lambda.
# Original list of integers:
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squ = lambda i : i**2
cub = lambda i : i**3

squaredli = [(squ(i),cub(i)) for i in li ]

print(squaredli)