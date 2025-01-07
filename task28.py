'''a Python program to remove duplicates from a list while preserving the
order of elements'''

orgList = ["mub",1,"len",1,"forg","kijsk","raman","mub",4,45,9,4]
DuplicateRemovedList = []
[DuplicateRemovedList.append(i) for i in orgList if i not in DuplicateRemovedList]

print(DuplicateRemovedList)