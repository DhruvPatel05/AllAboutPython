class Mammals:
    def walk(self):
        print("walk")
class Dog(Mammals):
    def bark(self):
        print("bark")


class Cat(Mammals):
    def be_annoying(self):
        print("be_annoying")

dog1 = Dog()
cat1 = Cat()
dog1.walk()
dog1.bark()
cat1.walk()
cat1.be_annoying()