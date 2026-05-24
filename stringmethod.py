#validate user input exercise
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

username = input("Enter username : ")
result = username.find(" ")
if len(username) > 12 :
    print("User name must not be more than 12.")
elif not result == -1 :
    print("Username can't contain spaces ")
elif not username.isalpha():
    print("Usename can't contain digits.")
else :
    print(f"Hello {username}")
