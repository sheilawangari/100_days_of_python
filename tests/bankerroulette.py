# Write a program that will select a random name from a list of names
# The person selected will have to pay for everybody's food bill 
# You are not allowed to use the choice() function
# names_string splits the string into individual names and puts them inside a List called names


import random 

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items - 1)     # its -1 because we start counting from index 0 
person_to_pay = names[random_choice]

print(person_to_pay + " is going to pay the bill today!")


