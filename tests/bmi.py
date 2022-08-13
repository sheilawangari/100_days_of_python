# Write a program that calculates the BMI from a user's weight and height
# The BMI is calculated by dividing a person's weight (in Kg) by the square of their height in (in m) 

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

print(type(height))
print(type(weight)) 
                                        # the weight converted to an int because the its of type string
bmi = int(weight) / float(height) ** 2  # the height has to be a float because we are looking for a number between 1 and 2
bmi_as_int = int(bmi)
print(bmi_as_int)