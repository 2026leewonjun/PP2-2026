#Person class

class Person:
    def __init__(self, name, mobile=None, office=None, email=None):
        self.name = name
        self.mobile = mobile
        self.office = office
        self.email = email

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMobile(self, mobile):
        self.mobile = mobile

    def getMobile(self):
        return self.mobile

    def setOffice(self, office):
        self.office = office

    def getOffice(self):
        return self.office

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def __str__(self):
        return str(self.name) + ", " + str(self.mobile) + ", " + str(self.office) + ", " + str(self.email)

p1 = Person("Kim", office="1234567", email="kim@company.com")
p2 = Person("Park", office="2345678")
p2.setEmail("park@company.com")

print(p1)
print(p2)