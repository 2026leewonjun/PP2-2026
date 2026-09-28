#Triangle class

class Triangle:
    numberOfSides = 3

    def __init__(self, a1, a2, a3):
        self.angle1 = a1
        self.angle2 = a2
        self.angle3 = a3

    def setAngle1(self, a1):
        self.angle1 = a1

    def getAngle1(self):
        return self.angle1

    def setAngle2(self, a2):
        self.angle2 = a2

    def getAngle2(self):
        return self.angle2

    def setAngle3(self, a3):
        self.angle3 = a3

    def getAngle3(self):
        return self.angle3

    def checkAngles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False

    def __str__(self):
        return "(" + str(self.angle1) + ", " + str(self.angle2) + ", " + str(self.angle3) + ")"

triangle = Triangle(90, 30, 60)
print(triangle.checkAngles())