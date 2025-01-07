#Create a Python function that takes a list as input and removes duplicate
#elements, preserving the order of the elements. Return the new list

lists = [1, 2, 3, 4, 5, 1, 2, 4, 6, 8, 5, 9, 5]
newList = []

for value in lists:
    if value not in newList:
        newList.append(value)

print(newList)







