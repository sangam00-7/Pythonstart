# variables : A container for a value (string, integer, float, boolean)
# A variable behaves as if it was the value it contains.

#string: A string is a series of character which can include numbers but we treat them as characters.

first_name = "Sangam"
age = "21"
email = "sangam123@gmail.com"
print(f"My name is {first_name}")
print(f"My age is {age}")
print(f"My email is {email} ")

#integer: An integer is a whole number.

roll_no = 12
print(roll_no)
# or
print(f"My roll no is {roll_no}")

#float: A float is a whole number which contains decimal portion.

price = 12.99
print(price)
#or
print(f"Price is {price}")

#Boolean: data type which is either true or false. They are binary.

a = True
b = False

if a:
    print("True")
else:
    print("False")