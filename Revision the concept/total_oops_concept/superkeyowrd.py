#  Super Method

class Car:
    def __init__(self,type):
        self.type = type


    @staticmethod
    def start():
        print("Car is Started...")

    @staticmethod
    def stop():
        print("Car is stopped...")

class Toyota(Car):
    def __init__(self, name,type):
        super().__init__(type)
        self.name = name
        super().start()


car1 = Toyota("Fortuner","electric")
print(car1.type)
