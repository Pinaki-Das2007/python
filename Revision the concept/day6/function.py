## Funtion

# a = 12
# b = 45
# c = 36

# avg = (a + b + c) / 3
# print(avg)

# Function defination
def avg():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    c = int(input("Enter third number:"))
    average = (a+b+c)/3
    print("Average of three numbers is :",average)

# Function call
avg()

for i in range(5):
    avg()
    print("Thank you for using this function.")

