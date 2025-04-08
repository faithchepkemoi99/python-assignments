# encapsulate keeping attributes and methods private to prevent unwanted disturbance
def __init__(self):
    self.__chocolate = 10 #private attribute

    def take_chocolate(self):
        if self.__chocolates > 0:
            