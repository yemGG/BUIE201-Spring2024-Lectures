class Apple:

    def __init__(self, color, type, x) -> None:
        self.color = color
        self.type = type
        self.x = x
        self.q = 0

    def fall(self, y):
        self.x -= y


redamasya = Apple("red", "amasya", 2)
greenx = Apple("green", "x", 3)

redamasya.fall(3)

greenx.q = 99

print (greenx.q)

print (redamasya.q)
