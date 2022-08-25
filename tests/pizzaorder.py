# An automatic pizza order program 

print("Welcome to Python Pizza Deliveries! ")

size_of_pizza = input("What size of pizza do you want? S, M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ") 

bill = 0

if size_of_pizza == "S":
  bill += 15 

elif size_of_pizza == "M":
  bill += 20 

elif size_of_pizza == "L":
  bill += 25 

if add_pepperoni == "Y":
  if size_of_pizza == "S":
    bill += 2 

  else:
    bill += 3 

if extra_cheese == "Y":
  bill += 1  

print(f"Your final bill is ${bill}")