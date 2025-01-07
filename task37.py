from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass
    @abstractmethod
    def calculatePerimeter(self):
        pass
class circle(Shape):
    def calculateArea(self,radius):
        area = 3.14 * (radius ** 2)
        print(area)
    def calculatePerimeter(self,radius):
        primeter = 2*3.14*radius
        print(primeter)
        




class Triangle(Shape):
    def calculateArea(self,base,height):
        area = 1/2*(base*height)
        print(area)
    def calculatePerimeter(self,a,b,c):
        primeter = a+b+c
        print(primeter)
c1= circle()
c1.calculateArea(5)
c1.calculatePerimeter(5)

t1 = Triangle()
t1.calculateArea(6,7)
t1.calculatePerimeter(4,5,6)