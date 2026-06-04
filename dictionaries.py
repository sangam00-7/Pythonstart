#Dictionaries = A collection of {key : value} pairs ordered and changeable , No duplicates
capitals = {"Nepal": "Kathmandu",
            "India" :"New Delhi",
            "China" : "Beijing"}
#print(capitals.get("Nepal"))
#if capitals.get("Japan"):
#    print("That capital exit.")
#else:
#    print("That capital doesn't exist")
capitals.update({"Srilanka": "Columbus"}) #updates and add key : value
print(capitals)

capitals.pop("China") #Removes key and value from dictionary
 
 # to clear = dictionary.clear()
 
key = capitals.keys()
print(key)

value = capitals.values()
print(value)

#item = capitals.items()
for key,value in capitals.items():
 print(f"{key}:{value}")