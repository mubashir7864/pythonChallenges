'''Convert two lists into a dictionary in Python without using a built-in method'''

keys = ["name","age","address","state","pincode"]
values = ["zaid",24,"ejipura","karnataka",560089]
dict1 = {}
for i in range(len(keys)):
    dict1[keys[i]] = values[i]


print(dict1.items())
print(type(dict1))

print(dict1["name"])