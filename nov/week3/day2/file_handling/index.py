# file = open("students.txt", "x")
# file.close()
# print("students file created...")


# file = open("students.txt","r")
# print("opened")
# file.close()

# file = open("students.txt","r")
# info = file.read()
# print(info)
# file.close()


# file = open("students.txt","r")
# info = file.readline()
# print(info)
# file.close()


file = open("students.txt","r")
file.write("this is new line for student 4")
file.close()
print("new text added in student file")

