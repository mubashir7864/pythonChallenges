#You are given an array arr[] of non-negative integers.
#  Your task is to move all the zeros in the array to the 
# right end while maintaining the relative order of the non-zero elements.
#  The operation must be performed in place,
#  meaning you should not use extra space for another array.

# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.
# Input: arr[] = [10, 20, 30]
# Output: [10, 20, 30]
# Explanation: No change in array as there are no 0s.
# Input: arr[] = [0, 0]
# Output: [0, 0]
# Explanation: No change in array as there are all 0s.

def ar(arr):
    leng =len(arr)
    i=0
    while i < leng:
        if arr[i] == 0:
            arr.pop(i)
        else:
            i += 1
    lent = leng - len(arr)
    for _ in range(lent):
        arr.append(0)

    return  arr

arre= [10, 20, 30]
arrf =  [0, 0]



print(ar(arre))
print(ar(arrf))
