## Sets are a collection of unique elements. They are unordered, meaning that the elements do not have a specific order, and they do not allow duplicate values. Sets are commonly used in programming to perform operations such as union, intersection, and difference between collections of data. In Python, sets can be created using curly braces {} or the set() constructor.

## Creating a set

my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))

my_empty_set = set([1,2,3,4,5])
print(my_empty_set)
print(type(my_empty_set))

my_dictionary = {1: 'one', 2: 'two', 3: 'three'}
print(my_dictionary)
print(type(my_dictionary))

my_dup_set = {1, 2, 3,3, 4, 5, 5, 5}
print(my_dup_set)
print(type(my_dup_set))

test_set  = {1, 2, 3, 4, 5}


## 
test_set.add(6)
print(test_set)
test_set.add(6)
print(test_set)

test_set.remove(6)
print(test_set)

test_set.discard(6)
print(test_set)

## Pop method

removed_element = test_set.pop()
print(removed_element)
print(test_set)

removed_element = test_set.pop()
print(removed_element)
print(test_set)

test_set.clear()
print(test_set)


## Set Membership testing
new_set = {1, 2, 3, 4, 5}
print(1 in new_set)
print(6 in new_set)

## mathemetical operations on sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1.union(set2)
print(union_set)

interesection_set = set1.intersection(set2)
print(interesection_set)

difference_set = set1.difference(set2)
print(difference_set)

set1.intersection_update(set2)
print(set1)



set2.difference_update(set1)
print(set2)


##Symetric difference 

new_set1 = {1, 2, 3, 4, 5}
new_set2 = {4, 5, 6, 7, 8}

sym_dif = new_set1.symmetric_difference(new_set2)
print(sym_dif)

