#  Methods that don't use self are known as static methods in python and they work at class level

class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    @staticmethod  # decorator
    def heelo():
        print("Hello")


    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your average score is:",sum/3)

s1 = Student("Karan", [10,20,30])
s2 = Student("Arjun", [40,50,60])
s1.get_avg()
s2.get_avg()
s1.heelo()