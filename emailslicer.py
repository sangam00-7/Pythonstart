email = input("Enter your email : ")

index = email.index("@")

user = email[:index]
domain = email[index:]

print(f"User is {user}")
print(f"Domain is {domain}")