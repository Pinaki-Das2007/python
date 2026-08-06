marks = {
    "harry" : 85,
    "rohan " : 78,
    "subham" : 98,
    "shubham" : 45,
    0:"pinaki"
}

print(marks['harry'])
print(marks['rohan '])
print(marks[0])

## It is unordered
## It is mutable
## It is indexed

print(marks.items())
print(marks.keys())

marks.update({"harry": 90})
print(marks)


## Get method

print(marks.get("harry2"))
print(marks["harry2"])

