#1.	Implement a Python program to swap two numbers without using a third variable.

a = 5
b = 10

print("Before swapping: a =", a, ", b =", b)
a, b = b, a  # Swapping using tuple unpacking
print("After swapping: a =", a, ", b =", b)