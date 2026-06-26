## Packing and unpacking of tuples

packed_tuple = 1,"hello",3.14
print(packed_tuple)

a,b,c = packed_tuple
print(a)
print(b)
print(c)

## unpacking of tuples using *

numbers=(1,2,3,4,5,6)
first,*middle,last = numbers
print(first)
print(middle)
print(last)

## Nested tupple
lst = [[1,2,3],[4,5,6],["hello","world",3.14]]  ##nested list
print(lst[0][0:3])



tup = ((1,2,3),(4,5,6),("hello","world",3.14))  ##nested tuple
print(tup[0][0:3])


## iteration

for sub_tuple in tup :
    for item in sub_tuple:
        print(item,end =" ")
    print()