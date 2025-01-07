#Write a function in Python to count words in a text file those are ending with
#alphabet "e".


def countwords(filename):
    count = 0
    with open(filename, 'r') as file:
        for eachLine in file:
            words = eachLine.split()  
            for word in words:
                if word.lower().endswith('e'):
                    count += 1
    return count

filename = 'story.txt'
result = countwords(filename)
print(f"No of words ending with e :  {result}")
