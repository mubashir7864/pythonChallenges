'''a Python function that takes a list and an element as input and counts how
many times that element appears in the list.'''

listjululu = ["great",1,21,21,3,6,4,5,8,1.5,21,3,5,"great",1.5]

def countOccurance(list_,elementName):
    count = 0
    for i in list_:
        if i == elementName:
            count += 1
    print(f"{elementName} in given list is appeared {count} times")

countOccurance(listjululu,21)

         
