'''a Python program that takes a list of person tuples (name, age) and
calculates and prints the average age of the group'''

persons = [("Mubashir",30),("Fazal",34),("shukoor",45),("jafar",23),("sukumari",25)]

def ageAverage(lists):
    sum=0
    avg = 0
    listLength = len(lists)
    for i,j in persons:
        sum += j
        
    avg = sum/listLength
    return int(avg)

print(ageAverage(persons))