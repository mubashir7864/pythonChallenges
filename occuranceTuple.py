'''a Python function that takes tuple and an element as input and counts how
many times that element appears in the tuple.'''

tuplejululu = ("great",1,21,21,3,6,4,5,8,1.5,21,3,5,"great",1.5)

print(type(tuplejululu))

def countOccurance(tuple_,elementName):
    count = 0
    for i in tuple_:
        if i == elementName:
            count += 1
    print(f"{elementName} in given tuple is appeared {count} times")

countOccurance(tuplejululu,"great")