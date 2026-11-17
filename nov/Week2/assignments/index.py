# LIST

# 1
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for num in numbers:
    print(num)


# 2
numbers = [10, 11, 530, 320, 111, 30, 10]

for num in numbers:
    if num % 2 == 0:
        print(num, "even")
    else:
        print(num, "odd")


# 3
numbers = [10, 20, 500, 300, 111, 30, 10]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)


# 4
numbers = [10, 20, 10, 30, 10, 40, 50]

count = 0
target = 10

for num in numbers:
    if num == target:
        count += 1

print(count)


# 5
def total(numbers):
    result = 0

    for num in numbers:
        result += num

    return result

numbers = [10, 20, 30, 40, 50]
print(total(numbers))


# 6
numbers = [10, 20, 500, 300, 111, 30]

largest = numbers[0]
second = numbers[0]

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)


# 7
numbers = [10, 20, 30, 10, 40, 20, 50]

new_list = []

for num in numbers:
    if num not in new_list:
        new_list.append(num)

print(new_list)


# 8
numbers = [10, -20, 0, 30, -40, 0, 50]

positive = []
negative = []
zero = []

for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zero.append(num)

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)


# 9
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = []

for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print(common)


# 10
def palindrome(numbers):
    for i in range(len(numbers)):
        if numbers[i] != numbers[len(numbers) - 1 - i]:
            return False

    return True

numbers = [10, 20, 30, 20, 10]
print(palindrome(numbers))



# TUPLE

# 1
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

for num in numbers:
    print(num)


# 2
numbers = (10, 20, 30, 40, 50)

for index, num in enumerate(numbers):
    print(index, num)


# 3
numbers = (10, 20, 500, 300, 111, 30)

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)


# 4
numbers = (10, 20, 10, 30, 10, 40, 50)

print(numbers.count(10))


# 5
numbers = (10, 20, 30, 40, 50)

total = 0

for num in numbers:
    total += num

print(total)


# 6
numbers = (10, 20, 500, 300, 111, 30)

largest = numbers[0]
second = numbers[0]

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)


# 7
numbers = (10, 20, 30, 10, 40, 20, 50)

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print(duplicates)


# 8
numbers = (10, 20, 30, 20, 10)

result = True

for i in range(len(numbers)):
    if numbers[i] != numbers[len(numbers) - 1 - i]:
        result = False
        break

print(result)


# 9
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)

common = []

for num in tuple1:
    if num in tuple2 and num not in common:
        common.append(num)

print(common)


# 10
numbers = (10, 11, 20, 21, 30, 31, 40)

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even:", even)
print("Odd:", odd)



# SET

# 1
numbers = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}

for num in numbers:
    print(num)


# 2
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print(set1.union(set2))


# 3
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print(set1.intersection(set2))


# 4
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print(set1.difference(set2))


# 5
numbers = {10, 20, 500, 300, 111, 30}

first = True

for num in numbers:
    if first:
        largest = num
        smallest = num
        first = False
    else:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

print("Largest:", largest)
print("Smallest:", smallest)


# 6
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

common = set()

for num in set1:
    if num in set2:
        common.add(num)

print(common)


# 7
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

result = set1.copy()

for num in set2:
    result.add(num)

print(result)


# 8
set1 = {10, 20, 30}
set2 = {30, 20, 10}

if set1.issubset(set2) and set2.issubset(set1):
    print("Both sets are equal")
else:
    print("Both sets are not equal")


# 9
set1 = {10, 20, 30, 40}
set2 = {20, 30, 50, 60}
set3 = {30, 40, 70, 80}

all_sets = set1.union(set2, set3)

result = set()

for num in all_sets:
    count = 0

    if num in set1:
        count += 1
    if num in set2:
        count += 1
    if num in set3:
        count += 1

    if count == 1:
        result.add(num)

print(result)


# 10
str1 = "hello"
str2 = "world"

common = set()

for ch in str1:
    if ch in str2:
        common.add(ch)

print(common)



# DICTIONARY

# 1
students = {
    "Rahul": 85,
    "Amit": 70,
    "Ravi": 90,
    "Sumit": 35,
    "Rohit": 60
}

for name, marks in students.items():
    print(name, marks)


# 2
student = {
    "name": "Rahul",
    "age": 20
}

student["city"] = "Bhubaneswar"

print(student)


# 3
students = {
    "Rahul": 85,
    "Amit": 70,
    "Ravi": 90
}

students["Rahul"] = 95

print(students)


# 4
students = {
    "Rahul": 85,
    "Amit": 70,
    "Ravi": 90,
    "Sumit": 35,
    "Rohit": 60
}

total = 0

for marks in students.values():
    total += marks

print("Total marks:", total)


# 5
students = {
    "Rahul": 85,
    "Amit": 70,
    "Ravi": 90,
    "Sumit": 35,
    "Rohit": 30
}

passed = 0
failed = 0

for marks in students.values():
    if marks >= 40:
        passed += 1
    else:
        failed += 1

print("Passed:", passed)
print("Failed:", failed)


# 6
students = {
    "Rahul": 85,
    "Amit": 70,
    "Ravi": 90,
    "Sumit": 35,
    "Rohit": 60
}

first = True

for name, marks in students.items():
    if first:
        highest = marks
        lowest = marks
        high_name = name
        low_name = name
        first = False
    else:
        if marks > highest:
            highest = marks
            high_name = name

        if marks < lowest:
            lowest = marks
            low_name = name

print("Highest:", high_name, highest)
print("Lowest:", low_name, lowest)


# 7
students = {
    "Rahul": 85,
    "Amit": 70,
    "Ravi": 90,
    "Sumit": 35,
    "Rohit": 60
}

highest = 0
second = 0

for marks in students.values():
    if marks > highest:
        second = highest
        highest = marks
    elif marks > second and marks != highest:
        second = marks

print("Second highest marks:", second)


# 8
students = {
    "Rahul": 85,
    "Amit": 70,
    "Ravi": 90,
    "Sumit": 35,
    "Rohit": 60
}

new_students = {}

for name, marks in students.items():
    if marks > 75:
        new_students[name] = marks

print(new_students)


# 9
string = "programming"

frequency = {}

for ch in string:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print(frequency)


# 10
dict1 = {
    "name": "Rahul",
    "age": 20
}

dict2 = {
    "city": "Bhubaneswar",
    "marks": 85
}

dict3 = {}

for key, value in dict1.items():
    dict3[key] = value

for key, value in dict2.items():
    dict3[key] = value

print(dict3)