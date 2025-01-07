# Write a function in python to count the number of lines from a text file "story.txt"
# which is not starting with an alphabet "T"

def countlines(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if not line.strip().startswith('t'):
                count += 1
    return count


filename = 'story.txt'
result = countlines(filename)
print(f"No of lines not starting with 'T': {result}")
