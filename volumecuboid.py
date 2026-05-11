# Volume of a cuboid

length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))
height = float(input("Enter the height: "))
unit=input("Enter unit (m/cm/k) :")

volume = length * breadth * height

print(f"The volume of the cuboid is {volume} {unit}^3")