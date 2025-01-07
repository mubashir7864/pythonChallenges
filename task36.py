from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class lion(Animal):
    def sound(self):
        print("sounds Roar....")
class Tiger(Animal):
    def sound(self):
        print("sounds kharrr...")
tiger = Tiger()
tiger.sound()

li = lion()
li.sound()