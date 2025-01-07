class person:
    schoolName  = "Commomn"

    def __init__(self,name,age):
        self.name= name
        self.age = age

    def changeSc(cls,name):
        cls.name= name

person.changeSc(person,"nomaki")

print(person.schoolName)
    