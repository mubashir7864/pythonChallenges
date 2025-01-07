#Write a program to create an iterator to print English alphabets from A to Z


class AlphabetIter:

    def __init__(self):
        self.current = ord("A")

    def __iter__(self):
        return(self)
    
    def __next__(self):
        if self.current <= ord("Z"):
            letter = chr(self.current)
            self.current += 1
            return letter
        else:
            raise StopIteration
    
alpha = AlphabetIter()
for i in alpha:
    print(i, end=",")

