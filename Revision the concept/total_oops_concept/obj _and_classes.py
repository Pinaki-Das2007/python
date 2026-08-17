class Student:

    # default constructor
    def __init__(self):
        pass

    #parameterized constructor
    def __init__ (self,name,rollno):
        self.name = name
        self.rollno = rollno

        print("Adding a new student into the database")

   


s1 = Student("karan",34)
print(s1.name,s1.rollno)

s2= Student("arjun",45)
print(s2.name,s2.rollno)