numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers[2:5])
# print(numbers[:5])
# print(numbers[5:])
# print(numbers[::2])
# print(numbers[::-1])
# print(numbers[::3])
# print(numbers[::-2])


# for number in numbers:
#     print(number)


for index,number in enumerate(numbers):
    print(index,number)

## list comprehension

lst = []

# for x in range(10):
#     lst.append(x**2)


# print(lst)


[x**2 for x in range(10)]
print([x**2 for x in range(10)])