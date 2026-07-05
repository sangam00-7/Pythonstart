num = float(input("Enter first number: "))

while True:
    sign = input("Enter sign (+, -, *, /) or = to exit: ")

    if sign == "=":
        print("Final Result =", num)
        break

    num2 = float(input("Enter next number: "))

    if sign == "+":
        num = num + num2

    elif sign == "-":
        num = num - num2

    elif sign == "*":
        num = num * num2

    elif sign == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            continue
        num = num / num2

    else:
        print("Invalid sign.")
        continue

    print("Result =", num)
print("Successfull")