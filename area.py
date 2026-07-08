#calculating area of a rectangle

length = float(input("Enter length: "))
breadth =float (input("Enter breadth: "))
area = length * breadth
print(f"Area of a rectangle is {area} m^2")

#shopping cart program

item =input("Which item do you want to buy ? ")  #while working with string we don't need type casting.
price = float(input("What is the price ? "))
quantity=int(input("How many do you want ? "))

print(f"Name of a item is :{item}.")
print(f"Price is : {price}.")
print(f"I want {quantity} items.")
print("Successfull")