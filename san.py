num = int(input("Enter how many times you want to print your name: "))
name = input("Enter your name: ")

for i in range(num):
    print(name)

#using while

num = int(input("Enter how many times you want to print your name: "))
name = input("Enter your name: ")

count = 1

while count <= num:
    print(name)
    count += 1