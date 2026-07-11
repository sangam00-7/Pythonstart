#weight conversion

weight = float(input("Enter your weight : "))
unit = input("Kilograms or pounds ? (k or l) : ")

if unit == "k" :
    result = weight * 2.2
    print(f"Your weight is {round(result,2)} pounds.")
elif unit == "l" :
    result = weight / 2.2
    print(f"Your weight is {round(result,2)} Kilos.")
else :
    print("Invalid unit. Please enter correct unit. ")