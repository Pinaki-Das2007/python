class employee:
        a = 1

class programmer(employee):
    b = 2

class manager(programmer):
    c = 3

o = employee()
print(o.a)  # Pints the a attribute 
# print(o.b) # shows an error as there is no b attribute  in employee class


o = programmer()
print(o.a)
print(o.b)
# print(o.c) # shows an error as there is no c attribute in programmer class

o = manager()
print(o.a)
print(o.b)
print(o.c)
