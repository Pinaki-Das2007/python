class Account():
    def __init__ (self,balance, account_no):
        self.balance = balance
        self.account_np = account_no


    def debit(self,amount):
        self.balance = self.balance - amount
        print("Rs.", amount ,"was debited, your current balance is Rs.", self.balance)

    def credit(self,amount):
        self.balance = self.balance + amount
        print("Rs.", amount ,"was credited, your current balance is Rs.", self.balance)


acc1 = Account(5000, 1234)
print(acc1.balance)
print(acc1.account_no)



