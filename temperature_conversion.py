#temperature conversion

temperature = float(input("Enter temperature : "))
unit = input("elsius or  Fahrenheit (c or f ?) ")

if unit == "c" :
    result = temperature + 33.8
    print(f"Temperature is {result} Fahrenheit ")
elif unit =="f" :
    result = temperature - 33.8
    print(f"Temperature is {result} celsius ")
else :
    print("Invalid unit.")