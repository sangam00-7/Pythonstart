#Rectangle structure
rows = int(input("Enter no of rows: "))
column = int(input("Enter no of columns: "))
symbol = input("Enter symbol:")

for x in range (rows):
    for y in range(column):
        print(symbol,end="")
    print()


#


#Triangle

rows = int(input("Enter no of rows: "))
symbol = input("Enter symbol:")

for x in range (rows):
    for y in range(x+1):
        print(symbol,end="")
    print()
