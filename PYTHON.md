# 🐍 Python Notes

Quick reference notes for Python basics, OOP, and Data Science libraries.

---

## 🚀 Getting Started
- Python is **interpreted, high-level, and dynamically typed**.
- Great for **AI/ML, Data Science, Web Dev, Automation**.
- Run code with:  
  ```bash
  python filename.py


---

🔑 Basics

Hello World

print("Hello, World!")

Variables

x = 10        # int
name = "Anup" # string
pi = 3.14     # float
is_ai = True  # boolean

Data Types

int, float, str, bool

list, tuple, set, dict



---

📦 Collections

List

fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print(fruits[0])   # apple

Tuple

coords = (10, 20)

Set

unique = {1, 2, 3}

Dictionary

person = {"name": "Anup", "age": 20}
print(person["name"])


---

🔄 Control Flow

If-Else

age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")

Loops

for i in range(5):
    print(i)

while True:
    break


---

🛠️ Functions

def greet(name):
    return f"Hello, {name}"

print(greet("Anup"))


---

🏗️ OOP (Classes)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name}")

p = Person("Anup", 20)
p.greet()


---

📂 Modules & Packages

import math
print(math.sqrt(16))   # 4.0


---

⚡ Advanced Topics

List comprehensions

Lambda functions

Decorators

Generators

Error handling (try-except)

Virtual environments



---

📊 Python for Data Science

1. NumPy (Numerical Python)

import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.mean())      # Average
print(arr.shape)       # Shape of array

Supports multi-dimensional arrays (matrices).

Fast mathematical operations.



---

2. Pandas (Data Analysis)

import pandas as pd

data = {"Name": ["Anup", "Raj"], "Age": [20, 21]}
df = pd.DataFrame(data)

print(df.head())     # Show first rows
print(df["Name"])    # Access column

Series (1D) and DataFrame (2D).

Used for cleaning, manipulating, analyzing data.



---

3. Matplotlib (Data Visualization)

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.show()


---

4. Seaborn (Statistical Visualization)

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()


---

5. Scikit-Learn (Machine Learning)

from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

model = LinearRegression()
model.fit(X, y)

print(model.predict([[5]]))   # Predict y for x=5


---

6. TensorFlow / PyTorch (Deep Learning)

import tensorflow as tf

# Simple constant
hello = tf.constant("Hello, AI!")
print(hello.numpy().decode())

(Pytorch is also widely used for deep learning research.)