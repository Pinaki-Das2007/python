# Types of Inheritance
# 1. Single Inheritance
# 2. Multilevel Inheritance
# 3. Multilevel Inheritance

#  2. Multilevel Inheritance
class Car:
    @staticmethod
    def start():
        print("car started....")

    @staticmethod
    def stop():
        print("car stopped....")

class Toyota(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(Toyota):
    def __init__(self, type):
        self.type= type
        
car1 = Fortuner("Petrol")
print(car1.type)       
car1.start()


