class employee:
    language = "python"  # This is a class attribute
    salary = 1200000

harry = employee()
harry.language = "java"  # This is an object / instance attribute
print( harry.language, harry.salary)