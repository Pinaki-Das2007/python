class Person:
    __name = "anonymous"

    def __hello(self):
        print("Hello")

    def welcome(self):
        self.__hello()


p1 = Person()
print(p1.welcome())  # This will raise an AttributeError since __hello is private
