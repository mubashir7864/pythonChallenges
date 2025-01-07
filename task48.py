#Write a function in Python to count and display the total number of words in a
#text file

def countwords(filename):
    count = 0
    with open(filename, 'r') as file:
        for eachLine in file:
            words = eachLine.split()  
            for _ in words:
                    count += 1
    return count

filename = 'story.txt'
result = countwords(filename)
print(f"No of words :  {result}")