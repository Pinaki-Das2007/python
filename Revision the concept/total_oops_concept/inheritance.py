#  Inheritance
#  =======================================
#  When one class(child/derived) derives the properties & methods of another class(parent/base).

class Car:
    @staticmethod
    def start():
        print("Car started....")

    @staticmethod
    def stop():
        print("Car stopped....")


class BMW(Car):
    def __init__(self,name):
        self.name = name

car1 = BMW("BMW X5")
car2 = BMW("BMW X6")


print(car1.name)
print(car1.start())