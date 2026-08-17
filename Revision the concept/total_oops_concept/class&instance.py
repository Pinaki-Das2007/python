class Student:
    college_name = "GITA AUTONOMOUS COLLEGE"
    


    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database")


s1 = Student("Karan",34)
print(s1.name, s1.marks)

s2 = Student("Arjun",88)
print(s2.name, s2.marks)

print(s1.college_name)
print(s2.college_name)
print(Student.college_name)