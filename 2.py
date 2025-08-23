#2.	Create a program to display memory locations of two variables using id() function, 
# and then use identity operators to compare whether two objects are the same or not.

a = 20
b = 20
if (a is b):
    print("Line 1 - a and b have same identity")
else:
    print("Line 1 - a and b do not have same identity")
if (id(a) == id(b)):
    print("Line 2 - a and b have same identity")
    print("id - A ", id(a))
    print("id - B ", id(b))
else:
    print("Line 2 - a and b do not have same identity")
b = 30
if (a is b):
    print("Line 3 - a and b have same identity")
    print("id - A ", id(a))
    print("id - B ", id(b))
else:
    print("Line 3 -'a and b do not have same identity")
    print("id - A ", id(a))
    print("id - B ", id(b))
if (a is not b) :
    print("Line 4 - a and b do not have same identity")
else:
    print("Line 4 - a and b have same identity")