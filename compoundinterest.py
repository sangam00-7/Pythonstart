principle = 0
rate = 0
time = 0

while principle <=0 :
    principle = float(input("Enter principle : "))
    if principle <= 0:
        print("Principle can't be zero or negative number")



while rate <=0 :
    rate = float(input("Enter Rate : "))
    if rate <= 0:
        print("Rate can't be in zero or negative.")

while time <=0 :
    time = float(input("Enter Time : "))
    if time <= 0:
        print("Time can't be in zero or negative.")

total = principle * (1 + rate/100) ** time
print(f"Total is {total:.2f}")

#another approach


principle = 0
rate = 0
time = 0

while True :
    principle = float(input("Enter principle : "))
    if principle <= 0:
        print("Principle can't be zero or negative number")
    else :
        break



while True :
    rate = float(input("Enter Rate : "))
    if rate <= 0:
        print("Rate can't be in zero or negative.")
    else :
        break

while True:
    time = float(input("Enter Time : "))
    if time <= 0:
        print("Time can't be in zero or negative.")
    else :
        break

total = principle * (1 + rate/100) ** time
print(f"Total is {total:.2f}")



#while True
#     ↓
#Run code
#     ↓
#Condition met?
#   /      \
# No        Yes
# |          |
#Repeat    break
#             ↓
#           Stop