#parent class
class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def call(self):
        print(f"{self.brand} {self.model} is making a call")

    def info(self):
        print(f"This is a {self.brand} {self.model} smartphone.")

#inheritance

class SmartPhone(Phone):
    def browse_internet(self):
        print(f"{self.brand} {self.model} is browsing the internet.")

#creating objects
basic_phone = Phone("Motorola", "c13")
smart_phone = SmartPhone("Iphone", "16 Pro")

#using methods
basic_phone.info()
basic_phone.call()

smart_phone.info()
smart_phone.call()
smart_phone.browse_internet()

