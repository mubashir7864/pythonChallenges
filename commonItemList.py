''' a Python program that takes two lists and returns a new list containing
elements that are common in both input lists '''


list_1 = [1,2,10,14,5,365,8]
list_2 = [2,3,4,5,365,7,9,253]
newList =[]
def commonList(list1,list2):
    for i in list1:
        if i in list2:
            newList.append(i)
    return newList

print(commonList(list_1,list_2))