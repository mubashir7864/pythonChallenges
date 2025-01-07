'''a Python function that takes a dictionary of items and their prices as input
and finds and prints the keys (items) with the highest prices'''

dict1 = {"mango": 45,"orange":30,"kiwi": 100,"grapes":80,"fig":120}



def highestprice(dictt):
    temp = 0
    costlyItem = {}
    for i,j in dictt.items():
        if j >= temp:
            temp = j
            costlyItem ={i:j}
    return costlyItem

print(highestprice(dict1))

    

        
            
        



