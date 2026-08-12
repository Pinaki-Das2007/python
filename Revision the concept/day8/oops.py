class employee :
    name = "Harry"
    age = 25
    salary = 50000

harry = employee()
print(harry.name,harry.salary)

# Here name is object attribute and salary is class attribute. If we try to access the class attribute using object then  it will give us the value of class
#  attribute. But if we try to access the object attribute using class then it will give us the value of object attribute.