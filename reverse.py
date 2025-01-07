#Write a Python function that takes a list and returns a new list with the elements
#reversed. Do this without using the built-in reverse method.

lists = ["first","second","third","fourth","fifth","sixth"]



def reverssedList(originalList):
    newlist = []
    for i in originalList:
        newlist.insert(0,i)
    return newlist


print(reverssedList(lists))

