#countdown in forward order

#import time
#my_time =int(input("Enter the time in seconds : "))
#for x in range(0,my_time):
#    print(x)
#    time.sleep(1)
#print("Time's up!")


#countdown in reversed order

import time
my_time =int(input("Enter the time in seconds : "))
for x in reversed(range(0,my_time)):
    print(x)
    time.sleep(1)
print("Time's up!")