from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass
class circle(Shape):
    def calculateArea(self,radius):
        area = 3.14 * (radius ** 2)
        print(area)
class rectangle(Shape):
    def calculateArea(self,length,width):
        area = width * length
        print(area)
c1= circle()
c1.calculateArea(5)

r1  = rectangle()
r1.calculateArea(5,4)

