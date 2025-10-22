class Point:
    def move(self):
        print("Moving")
    def draw(self):
        print("Drawing")
point1 = Point()
point1.move()
point1.draw()
point1.x = 20
point1.y = 30
print(point1.x, point1.y)
point2 = Point()
point2.x = 40
print(point2.x)
