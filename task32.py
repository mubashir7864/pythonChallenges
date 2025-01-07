class Book:
    def __init__(self,bookName,Author,Year):
        self.bookName = bookName
        self.Author = Author
        self.Year = Year
    def bookInfo(self):
        print(f"BookName: {self.bookName}, Author: {self.Author}, Year: {self.Year}")

book1 = Book("The 5 AM Club", "Robin Shetty",2015)
book2 = Book("canon of medicine","IbnuSeena", 600)

book1.bookInfo()
book2.bookInfo()
