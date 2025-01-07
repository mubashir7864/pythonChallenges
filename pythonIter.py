class Ite:

    def __init__(self):
        self.items = []

    def __iter__(self):
        return self
    

    def __next__(self):
        if self == 5:
            StopIteration

obj = Ite()