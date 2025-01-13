'''a Python function that takes a dictionary of items and their prices as input
and finds and prints the keys (items) with the highest prices'''

dict1 = {"mango": 45,"orange":30,"kiwi": 100,"grapes":80,"fig":120}



def highPrice(dict1):
    temp = 0
    newdict = {}
    for i,j in dict1.items():
        if j > temp:
            temp = j
            newdict = {i:j}
         
    return newdict

print(highPrice(dict1))


    

        
            
        



