# Methods are functions that belong to object
class Student:
    college_name = "GITA AUTONOMOUS COLLEGE "

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student",self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Karan",34)
s1.welcome()
print(s1.get_marks())