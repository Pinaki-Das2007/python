#  A class method is a method which is bound to the class and not the object of the class. @classmethod decorator is uded to create a class method.
class employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")


e = employee()
e.a = 45
e.show()