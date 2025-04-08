#inheritance
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

class Car(Vehicle):
    pass

car =  Car(4)
print(car.wheels)


#polymorphism
class Dog:
    def speak(self):
        return 'woof'
       
class Cat:
    def speak(self):
        return 'meow'
#polymorphism in action
for animal in [Dog(), Cat()]:
       print(animal.speak())


#encapsulation
class SecretStash:
    def __init__(self):
        self.__chocolates = 10 #private attribute
    def take_chocolate(self):
        if self.__chocolates > 0:
            self.__chocolates -= 1
            print("one chocolate taken!")
        else:
            print("no chocolates left")

stash = SecretStash()
stash.take_chocolate()