num = int(input("Enter no of values: "))

total = 0

for x in range(num):
    number = float(input("Enter a float number: "))
    total = total + number

print("Sum =", total)