#collection = single "Variable" used to store multiple values.
#List = [] ordered and changeable. Duplicates Ok.
#set = {} unordered and imutable, but ADD/REMOVE OK. No duplicates
#Tuple = () ordered and unchangeable Duplicates OK. Faster 

#each value in collection is element.

#collection example using list


fruits = ["apple", "orange", "watermelon", "banana"]
#print(fruits)
#print(fruits[0]) #to print specific element
#print(fruits[0:2]) #to print upto which element is required

#for x in fruits :
#    print(x)

#in operator used to check element in list
print("apple" in fruits)

#lists are changeable
fruits[0]= "pineapple"
#print(fruits)

#list can be appended
fruits.append("apple")
#print(fruits)

# to insert
fruits.insert(0,"kiwi")
#print(fruits)

#to sort
fruits.sort()
#print(fruits)

#to reverse
fruits.reverse()
print(fruits) #to reverse in alphabetical order at first we have to sort the list

# to clear
#fruits.clear()
#print(fruits)

#to find index of element
print(fruits.index("kiwi"))

#to count
print(fruits.count("kiwi"))

#to find length or count all elements in list
print(len(fruits))

#Note :- dir() this function displays all the attributes and methods of any list,set or tuple

#help() :- This function gives description of methods 