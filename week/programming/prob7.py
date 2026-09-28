#PhoneBook class

class Person:
    def __init__(self, name, mobile=None, office=None, email=None):
        self.name = name
        self.mobile = mobile
        self.office = office
        self.email = email

    def __str__(self):
        res = self.name + "\n"
        if self.mobile:
            res += "mobile phone: " + str(self.mobile) + "\n"
        if self.office:
            res += "office phone: " + str(self.office) + "\n"
        if self.email:
            res += "email address: " + str(self.email) + "\n"
        return res

class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add(self, name, mobile=None, office=None, email=None):
        self.contacts[name] = Person(name, mobile, office, email)

    def __str__(self):
        result = ""
        for name in self.contacts:
            result += str(self.contacts[name]) + "\n"
        return result

obj = PhoneBook()
obj.add("Kim", office="1234567", email="kim@company.com")
obj.add("Park", office="2345678", email="park@company.com")
print(obj)