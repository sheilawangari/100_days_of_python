# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number. 

print("Welcome to the Love Calculator!")

name1 = input("What is your name?\n")
name2 = input("What is their name?\n") 

combined_string = name1 + name2              # this is will concantenate these two strings together
lower_case_string = combined_string.lower()       # We have to turn everything to lower case

t = lower_case_string.count("t")
r = lower_case_string.count("r")            # Checking for these specific letters in their combined names
u = lower_case_string.count("u")
e = lower_case_string.count("e") 

true = t + r + u + e                            # We can now add it all up, this is the first digit of the love score 

l = lower_case_string.count("l")
o = lower_case_string.count("o")            # Checking for these specific letters in their combined names
v = lower_case_string.count("v")
e = lower_case_string.count("e") 

love = l + o + v + e 

love_score = int(str(true)) + int(str(love))                 # Concantenate the tow love scores then convert to int


if (love_score) < 10 or (love_score) > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos.')

elif (love_score) >= 40 and (love_score) <= 50:
    print(f'Your score is {love_score}, you are alright together.') 

else:
    print(f'Your score is {love_score}.')
