# Given an array arr of integers, find all the elements that occur more than once in the array.
# If no element repeats, return an empty array.

def dup(arr):
    dic = {}
    newlist =[]
    if len(arr) == 0:
        return newlist
    for i in arr:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] +=1
    for k,v in dic.items():
        if dic[k] > 1:
            newlist.append(k)
    return newlist

print(dup([]))