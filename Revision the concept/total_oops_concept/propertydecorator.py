class Student():
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math


        #percentage
    @property
    def percentage(self):
        return (self.phy + self.chem + self.math)/3
        

stu1 = Student(90, 80, 70)
print(stu1.percentage)