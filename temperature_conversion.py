#temperature conversion

temperature = float(input("Enter temperature : "))
unit = input("elsius or  Fahrenheit (c or f ?) ")

if unit == "c" :
    result = (9/5)*temperature + 32
    print(f"Temperature is {result} Fahrenheit ")
elif unit =="f" :
    result = (temperature - 32) *(5/9)
    print(f"Temperature is {result} celsius ")
else :
    print("Invalid unit.")