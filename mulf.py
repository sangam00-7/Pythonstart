num = int(input("Enter no of values: "))

total = 1

for x in range(num):
    number = float(input("Enter a float number: "))
    total = total * number

print(f"Multiplication = {total:.2f} ")