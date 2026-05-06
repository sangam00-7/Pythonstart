# typecasting : The process of converting a value of one data type of another. (String, integer , float, boolean)
# Explicit vs Implicit

#Explicit typecasting

name = "Bro"
age = 19
gpa = 2.6
student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

#Explicit typecasting conversion

age = float(age)
print(type(age))
gpa = int(gpa)
print(type(gpa))
print(gpa)

# for boolean

student = str(student)
print(student)