#format specifiers = {value:flags} format a value based on what flags are inverted

#decimal precision

price1 = 4994.6728
price2 = 32512.891
price3 = -26156.272689

print(f"Price 1 is {price1:.2f}")
print(f"Price 2 is {price2:.2f}")
print(f"Price 3 is {price3:.3f}")


#padding = allocate some space to display the value

print(f"Price 1 is {price1:10}")
print(f"Price 2 is {price2:10}")
print(f"Price 3 is {price3:10}")

#sperator

print(f"Price 1 is {price1:,.2f}")
print(f"Price 2 is {price2:,.2f}")
print(f"Price 3 is {price3:,.3f}")

