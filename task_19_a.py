#Print the patterns.


for i in range(6):
    for k in range(i):
        print("#",end=",")
    print()
for i in range(6):
    for k in range(6-i):
        print("#",end=",")
    print()