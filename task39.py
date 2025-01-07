#Write a program to create a custom iterator that iterates from 1 to 10 in 0.5 intervals

class Ite:

    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self
    
    def __next__(self):
       rng = self.current
       if rng <= 10: 
            self.current += 0.5
            return rng 
       else:
           raise StopIteration
       
new = Ite()
print(next(new))
print(next(new))

for i in new:
    print(i,end=", ")
    