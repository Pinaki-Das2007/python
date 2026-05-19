# names = ["Pinaki","Krish","Jacob",1,2,3,4]
# print(names)

# mixed_list = [1,"Hello",3.14, True]
# print(mixed_list)     

#accesing list elements
fruits = ["apple","banana","chery","kiwi","mango"]
print(fruits[2])
print(fruits[0])
print(fruits[-1])
print(fruits[1:4])
print(fruits[1:4+1])
print(fruits[-1:-3])

## modifying list
fruits[2] = "watermelon"
print(fruits)



fruits.append("orange")
print(fruits)


fruits.insert(1,"grapes")
print(fruits)

fruits.remove("apple")
print(fruits)


popped_fruits = fruits.pop()
print(fruits)
print(popped_fruits)

print(fruits)
pooped_fruits2 = fruits.pop()
print(pooped_fruits2)


print(fruits)


index = fruits.index("banana")
print(index)

fruits.insert(1,"dragonfruit")
print(fruits)

