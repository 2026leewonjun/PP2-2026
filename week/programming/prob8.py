#Song class

class Song:
    def __init__(self, seq):
        self.seq = seq

    def sing(self):
        for line in self.seq:
            print(line)

aSong = Song(["TWINKLE, twinkle, little star,",
              "How I wonder what you are!",
              "Up above the world so high,",
              "Like a diamond in the sky."])
aSong.sing()