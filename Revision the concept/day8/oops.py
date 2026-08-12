class employee:
   
    language = "python"  # This is a class attribute
    salary = 1200000

harry = employee()
harry.name = "harry" # This is an object / instance  attribute
print(harry.name, harry.language, harry.salary)

rohan = employee()
rohan.name = "rohan roro rabinson"
print(rohan.name, rohan.salary, rohan.language)

# Here name is object / instance attribute and salary and language are class attributes. If we change the value of class attribute then it will be changed for all the objects of that class. But if we change the value of object attribute then it will be changed only for that object.
