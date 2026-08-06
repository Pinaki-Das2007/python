friends = ["Apple","orange",False,12.34,12]
print(friends[3])

friends[0] = "Grapes"  # Unlike strings lists are mutable
print(friends)
print(friends[0:3]) # slicing lists

friends.append("Banana")
print(friends)

l1 = [1,32,45,6,7,56,87]
print(l1)

l1.reverse()  # sorts the list in ascending order
print(l1)

l1.append(100)
l1.sort()  # sorts the list in ascending order

l1.insert(3, 333333)
print(l1)

l1.pop()  # removes the last element from the list
print(l1)

l1.remove(333333)
print(l1)

value = l1.pop(3)  # removes the element at index 3 and returns it
print(value)
print(l1)