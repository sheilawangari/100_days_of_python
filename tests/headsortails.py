import random 

random.randint(0, 1) 

toss = int(input("Please choose a number between 0 and 1: "))

if toss == 0:
    print("Tails")

elif toss == 1:
    print("Heads")

else:
    print("Please choose a number between 0 and 1")



