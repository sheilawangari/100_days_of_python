# Write a program that calculates the BMI from a user's weight and height
# The BMI is calculated by dividing a person's weight (in Kg) by the square of their height in (in m) 

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
 
                                        # the weight converted to an int because the its of type float
bmi = round(weight / height ** 2)  

if bmi < 18.5:
    print(f'Your BMI is {bmi}, you are underweight.')
elif bmi < 25:
    print(f'Your BMI is {bmi}, you have normal weight.')
elif bmi < 30:
    print(f'Your BMI is {bmi}, you are slightly overweight.')
elif bmi < 35:
    print(f'Your BMi is {bmi}, you are obese.')
else:
    print(f'Your BMI is {bmi}, you are clinically obese.')
