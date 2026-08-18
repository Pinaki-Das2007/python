# Class method
# ====================================
#  A class method is bound to the class & receives the class as an inplicit first argument.
#  Note - static method can't access or modify class state & generate for utility 


class Person:
    name = "anonymous"



    @classmethod
    def ChangeName(cls,name):
        cls.name = name


p1 = Person()
p1.ChangeName("Pinaki das")
print(p1.name)
print(Person.name) 