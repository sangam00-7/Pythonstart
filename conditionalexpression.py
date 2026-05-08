# A one-line shortcut for the if else statment(ternary operator).
# Formula = return X if our condition is true else return Y
# X if condition else Y

num = 5
result= "Even" if num % 2== 0 else "Odd"
print(result)

a=6
b=7
max_num=a if a>b else b
print(f"Maximum num is : {max_num}")

min_num= a if a<b else b
print(f"Minimum num is: {min_num}")