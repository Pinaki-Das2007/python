class employee:
    compant = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is  {self.company}.")

class coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the languages here is your language: {self.language}")


class programmer(employee,coder):
    company = "ITC infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language.")

a = employee()
b = programmer()

b.show()
b.printLanguage()
b.showLanguage()