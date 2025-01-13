''' a Python program that takes two lists and returns a new list containing
elements that are common in both input lists '''

li1 = [1,2,3,4,5,67,85,9]
li2 = [5,4,8,9,6,4,2,3,5]

liset = set(li1).intersection(set(li2))

print(liset)

def commonlist(ar1,ar2):
    newlist =[]
    for i in ar1:
        for j in ar2:
            if i == j:
                newlist.append(i)
    return newlist

print(commonlist(li1,li2))