class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("Moving")
    def draw(self):
        print("Drawing")

point1 = Point(1, 2)
point1.x = 12
print(point1.x, point1.y)

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")

person1 = Person("Shakira")
person1.talk()
person2 = Person("Dhruv")
person2.talk()