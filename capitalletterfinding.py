

def capital_indexes(strc):
    CapitalList =[]
    for i,char in enumerate(strc):
        if ord(char) >= 65 and ord(char) <= 90:
            CapitalList.append(i)
    
    return CapitalList
    
x = capital_indexes("HeLlO")

print(x)