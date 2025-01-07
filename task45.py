# Write a Python program to calculate the sum of the positive and negative numbers
# of a given list of numbers using the lambda function.

listNum= [1,5,6,8,7,-2,-6,-8,8,-6,-9,-7]

positiveNum = sum(filter(lambda n : n>=0,listNum))
negativeSum = sum(filter(lambda n : n<=0,listNum))

print(positiveNum,negativeSum)