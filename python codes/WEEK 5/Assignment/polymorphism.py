class Animal:
    def move(self):
        print("Animal is moving")

class Dog(Animal):
    def move(self):
        print("Dog is running")

class Bird(Animal):
    def move(self):
        print("Bird is flying")

class Fish(Animal):
    def move(self):
        print("Fish is swimming")

#list animals
animals = [Dog(), Bird(), Fish()]

#loop and call move
for animal in animals:
    animal.move()
