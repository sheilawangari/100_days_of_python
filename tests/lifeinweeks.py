# Create a program using maths and fstrings that tells us how many days, weeks, months we have left if we live until 90 years old

age = input("Whats your current age: ") 

age_as_int = int(age)

days = age_as_int * 365 
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")