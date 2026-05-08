#logical operators :- used on conditional statements
# and = checks two or more conditions if True
# or = checks if at least one condition is True
# not = True if condition is False, and vice versa

# and operator

temp = 70

if temp > 0 and temp < 35 :
    print("We have good weather.")
else:
    print("We have bad weather")


#or operator

temp =20
if temp < 0 or temp >30:
    print("Bad weather")
else :
    print("Good weather")


    #not operator

    sunny = True
    if not sunny :
        print("Cloduy")
    else :
        print("Sunny")