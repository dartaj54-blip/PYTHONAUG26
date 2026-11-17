# # list
# fruits = ["apple", "orange", "fruit1", "fruit2", "fruit3"]
# for i,fruit in enumerate(fruits):
#     print(i+1,"->",fruit)
#     #tuple
# fruits = ("apple", "orange", "fruit1", "fruit2", "fruit3")
# for i,fruit in enumerate(fruits):
#     print(i+1,"->",fruit)
#     #set
# fruits={"apple", "orange", "fruit1", "fruit2", "fruit3"}
# for i,fruit in enumerate(fruits):
#     print(fruit)

#     #dist
#     student = {
# "name": "taaj",
# "age": 18,
# "city" : "bbsr"
# }
#     for i,fruit in enumerate(fruits):
#     print(fruit)

#function
#simple function

# def welcome():
#     print("welcome to python")
#     welcome()
# # argument
# def welcome_with_name(name,age,city):
#     print("welcome", name)
#     print("welcome", age)
#     print("welcome", city)
#      #keyword argument
# welcome_with_name(age=21,name="rahul",city="bbsr")

# #default argument
# welcome_with_name()
#Veriable length argument
# def showargs(*numbers):
#     for i in numbers:
#         print(i)


# #         showargs(10,20,30,40)
# def welcomemsg():
#  msg = "welcome to"
#  print(msg)
#  welcomemsg()


#  print() -> show somthing
#  return -> keep the Value
#  return
# def welcome():
#  return "welcome to python"

# write a function that return number is even or odd ?

# def check_number(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# result = check_number(10)
# print(result)
# write a function that take a list of numbers and return the largest number
# numbers = [10,20,500,300,1111]

# def largest_number(numbers):
#     largest = numbers[0]

#     for num in numbers:
#         if num > largest:
#             largest = num

#     return largest


# numbers = [10, 20, 500, 300, 1111]

# print(largest_number(numbers))

# write a function that takes a list of numbers and return largest and smallest numbers
# numbers = [10,20,500,300,111,30,10]

# def find_largest_smallest(numbers):
#     largest = max(numbers)
#     smallest = min(numbers)

#     return largest, smallest


# numbers = [10, 20, 500, 300, 111, 30, 10]

# largest, smallest = find_largest_smallest(numbers)

# print("Largest number:", largest)
# print("Smallest number:", smallest)

# writr a function that take a arg as age and return voting eligibility
# -not aligible
# -aligible
# # -just 1
# def voting_eligibility(age):
#     if age < 18:
#         return "Not Eligible"
#     elif age == 18:
#         return "Just 18"
#     else:
#         return "Eligible"


# print(voting_eligibility(17))
# print(voting_eligibility(18))
# print(voting_eligibility(25))

# write a function that takes mark and show grade
# mark      grade
# 90-100  -> a
# 80-89   -> b
# 70-79   -> c
# 50-59   -> d  
# less the 50 -> fail

# def show_grade(mark):
#     if mark >= 90 and mark <= 100:
#         print("Grade A")
#     elif mark >= 80:
#         print("Grade B")
#     elif mark >= 70:
#         print("Grade C")
#     elif mark >= 50:
#         print("Grade D")
#     elif mark < 50:
#         print("Fail")
#     else:
#         print("fail")


# show_grade(95)

# writr a function that take a number list and show the numbers are even or odd
# numbers = [10,11,530,320,111,30,10]
# 10 - "even"
# 11 - "odd"
# 530 - "even"
# 320 - "even"
# 111 - "odd"
# 30 -even
# 10 - odd
# def check_even_odd(numbers):
#     for num in numbers:
#         if num % 2 == 0:
#             print(num, "- even")
#         else:
#             print(num, "- odd")


# numbers = [10, 11, 530, 320, 111, 30, 10]

# check_even_odd(numbers)
# writr a function that take a number list and show how manu even and odds are thair
# numbers = [10, 11, 530, 320, 111, 30, 10]
# odd numbers are 2 and even numbers are 5 
# def count_even_odd(numbers):
#     even = 0
#     odd = 0

#     for num in numbers:
#         if num % 2 == 0:
#             even += 1
#         else:
#             odd += 1

#     print("Even numbers are:", even)
#     print("Odd numbers are:", odd)


# numbers = [10, 11, 530, 320, 111, 30, 10]

# count_even_odd(numbers)
# writr a function with n as arg, that show the multiplcation table

# n = 5
# 5*1=1
# 5*2=10
# .
# .
# .
# .
# 5*10=50
# def multiplication_table(n):
#     for i in range(1, 11):
#         print(n, "x", i, "=", n * i)


# multiplication_table(5)






