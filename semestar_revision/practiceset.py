""" Question 1 """
print("Question 1")

name = input("Hello User !! Enter your name: ")
print("Hello " + name + "  Good afternoon !! Welcome to the world of Python Programming. Today we will learn about Strings in Python. Let's get started !!") 




""" Question 2 """
print("Question 2")
letter = ''' Dear <| Name |>,
            You are selected !
            <| Date |>'''


name = input("Enter your name: ")
date = input("Enter the date:")

print(letter.replace("<| Name |>", name).replace("<| Date |>", str(date)))


"""" Question 3"""
print("Question 3")

word = "Harry  is a  good boy"
print(name.find("  "))