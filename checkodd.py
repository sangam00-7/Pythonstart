num = input("Enter any number : ")

if num.isdigit():
    num = int(num)

    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

    print("Successful")
else:
    print("Enter an integer")