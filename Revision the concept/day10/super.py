class employee:
    def __init__ (self):
         print("Constructor of Employee")
    a = 1

class programmer(employee):
    def __init__ (self):
         print("Constructor of programmer")
    b = 2

class manager(programmer):
    def __init__ (self):
         super().__init__()
         print("Constructor of manager")
    c = 3

o = manager()
print(o.a)
print(o.b)
print(o.c)