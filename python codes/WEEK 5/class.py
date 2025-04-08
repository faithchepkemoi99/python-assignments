class Car:
    color = "red"
    model = "BMW"

    #method/behaviour to display car details
    def drive(self):  #self is like a pointer referring to instance of the class the method is in or instance of the class used to access attributes and methods within the class
        print("The car is driving")

my_car = Car() #create an instance of the Car class
my_car.drive() #call the drive method
print(my_car.color) #access the color/model attribute




class person:
    #constructor method to initialize the object
    def __init__(self, name, age, height):
        self.name =name #instance variable for name
        self.age = age # instance variable for age
        self.height = height
    



personDetails = person("John", 30, 54.5) #create an instance of the person class
print(personDetails.age) # access the name attribute

    