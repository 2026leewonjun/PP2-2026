#Rectangle class

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def setWidth(self, w):
        self.width = w

    def getWidth(self):
        return self.width

    def setHeight(self, h):
        self.height = h

    def getHeight(self):
        return self.height

    def getArea(self):
        return self.width * self.height

    def overlap(self, r):
        if (self.x < r.x + r.width and self.x + self.width > r.x and
            self.y < r.y + r.height and self.y + self.height > r.y):
            return True
        return False

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.width) + ", " + str(self.height) + ")"

r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(10, 10, 100, 100)

if r1.overlap(r2):
    print("r1과 r2는 서로 겹칩니다.")
else:
    print("r1과 r2는 서로 겹치지 않습니다.")