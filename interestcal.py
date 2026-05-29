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

Interest = (principle * rate * time)/100
print(f"Simple Interest is {Interest}")

Total = principle + Interest
print(f"Actual amount is {Total}.")
