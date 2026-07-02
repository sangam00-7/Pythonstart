#circumference
import math
radius = float(input("Enter radius : "))
circumference = 2 * math.pi * radius

print(f"Circumferenceof a circle is {circumference:.2f}")

#area

radius = float(input("Enter radius of a circle:"))
area = math.pi * radius **2
print(f"Area of a circle is {area:.2f} m^2")

#hypotenuse of right angle triangle

a=float(input("Enter a: "))
b=float(input("Enter b:"))
c= math.sqrt(pow(a,2)+pow(b,2))
print(f"Hypotenus of right angle triangle is : {c:.2f}")

print("Successfull")