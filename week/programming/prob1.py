#Cat class

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def __str__(self):
        return self.name + " " + str(self.age)

missy = Cat('Missy', 3)
lucky = Cat('Lucky', 5)
print(missy)
print(lucky)