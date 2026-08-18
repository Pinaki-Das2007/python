#  Private attributes & methods
# =================================================================
#  Private attributes and methods are meant to be used only within the class and are not accessible from outside the class.
#  To make an attribute or method private in python in generally we use __ to make it private.


class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # Private attribute

    def reset_pass(self):
        print(self.__acc_pass)  # This will raise an AttributeError since __acc_pass is private

acc1 = Account(12345, "mypassword")

print(acc1.acc_no)
print(acc1.reset_pass())  # This will raise an AttributeError since __acc_pass is private

