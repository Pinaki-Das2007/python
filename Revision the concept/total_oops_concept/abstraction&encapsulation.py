#  Abstraction
#  Hiding the implementation details of a class adn only showing the essential features to the user.

class Car:
    def __inti__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started...")

car1 = Car()
car1.start()
    


#  Encapsulation
#  Wrapping data and functions into a single unit (object).
