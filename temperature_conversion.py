#temperature conversion

temperature = float(input("Enter temperature : "))
unit = input("elsius or  Fahrenheit (c or f ?) ")

if unit == "c" :
    result = round((9/5)*temperature + 32,2)
    print(f"Temperature is {result} Fahrenheit ")
elif unit =="f" :
    result = round((temperature - 32) *(5/9),2)
    print(f"Temperature is {result} celsius ")
else :
    print("Invalid unit.")