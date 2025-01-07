# Write a Python program to sort a list of dictionaries using Lambda.
# Original list of dictionaries :

dictlist= [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color':
'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

dictlist.sort(key=lambda x : x["make"])

print(dictlist)



