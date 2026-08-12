class employee:
    language = "python"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")

    @staticmethod
    def greet(self):
        print("Hello, welcome to the company!")


harry = employee()
harry.language = "java"
harry.getInfo()
harry.greet()