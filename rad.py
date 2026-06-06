import random
#number = random.randint(1,10)
low = 1
high = 10
number = random.randint(low,high)
print(number)

#choice

options =("Rock", "Paper", "Scissor")
option=random.choice(options)
print(option)

#shuffle

number =["1", "2","3","4","5"]
random.shuffle(number)
print(number)