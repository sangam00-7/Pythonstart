list = [1,2,3,2,1]
list1 = list.copy()
list1.reverse()
if list == list1:
    print("It is palindrome.")
else:
    print("It is not a palindrome.")