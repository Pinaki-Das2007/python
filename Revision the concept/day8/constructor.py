class employee:
    language = "python"
    salary = 1200000

    def __init__ (self,name,language,salary): ## Dunder method which is called automatically when an object is created
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Good morning")

harry = employee("Harry", "javascript", 1900000)
# harry.name = "harry"
print(harry.name,harry.salary,harry.language)

    