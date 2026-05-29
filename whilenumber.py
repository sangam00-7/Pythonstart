num = int(input("Enter number from (1 - 10): "))

while num < 1 or num >10 :
    print(f"{num} is wrong number.")
    num = int(input("Enter number from (1 - 10): "))
print("Thank you.")