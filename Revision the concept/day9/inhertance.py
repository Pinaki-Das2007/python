class Employee:
    company = "Itc"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}.")


# class programmer:
#     company = "ITC infotech"
#     def show (self):
#         print(f"The name is {self.name} and the salary is {self.salary}.")

#     def showLanguage(self):
#         print(f"The name is {self.name} and  he is good with {self.language} language.")

class programmer(Employee):
    company = "ITC infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and  he is good with {self.language} language.")
        

a = Employee()
b = programmer()

print(a.company)
print(b.company) 