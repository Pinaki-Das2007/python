s = {1,2,3,4,5,5,5,6,6,6}
print(s)
print(type(s))


e = set() ## Never use s = {} as it will create an empty dictionary
print(type(e))

## Methods in set

print(s, type(s))

s.add(566)
print(s, type(s))

s.remove(1)
print(s)

