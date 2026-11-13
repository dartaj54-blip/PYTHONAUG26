
# Operators

# 1. Add two numbers
a = 10
b = 20
print(a + b)

# 2. Calculate remainder
a = 10
b = 3
print(a % b)

# 3. Square of a number
num = 5
print(num * num)

# 4. Compare two numbers
a = 10
b = 20
print(a > b)
print(a < b)
print(a == b)

# 5. Check number between 10 and 50
num = 25

if num >= 10 and num <= 50:
    print("Number is between 10 and 50")
else:
    print("Number is not between 10 and 50")


# Conditional Statements

# 1. Positive or Negative
num = 10

if num > 0:
    print("Positive")
else:
    print("Negative")

# 2. Even or Odd
num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Voting Eligibility
age = 18

if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")

# 4. Largest of two numbers
a = 20
b = 30

if a > b:
    print("A is largest")
else:
    print("B is largest")

# 5. Calculate Grades
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")

# 6. Positive, Negative or Zero
num = 0

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 7. Simple Calculator
a = 10
b = 5
operator = "+"

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
else:
    print("Invalid operator")


# Loops

# 1. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# 2. Print numbers from 10 to 1
i = 10

while i >= 1:
    print(i)
    i -= 1

# 3. Even numbers from 2 to 20
for i in range(2, 21, 2):
    print(i)

# 4. Odd numbers from 1 to 20
for i in range(1, 20, 2):
    print(i)

# 5. Multiplication table
num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 6. Numbers from 5 to 25 with step 5
for i in range(5, 26, 5):
    print(i)

# 7. Reverse order from 5 to 1
for i in range(5, 0, -1):
    print(i)

# 8. Sum of numbers from 1 to 10
total = 0

for i in range(1, 11):
    total = total + i

print(total)

# 9. Number pattern
for i in range(1, 6):
    print(i)

# 10. Star pattern
for i in range(1, 6):
    print("*" * i)
