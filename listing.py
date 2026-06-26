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



fruits.insert(1,"dragonfruit")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

fruits.clear()
print(fruits)



lst = [1,2,3,4,5]
print(lst)

lst[1] = "krish"
print(lst)

lst[0] = "Pinaki"
print(lst)