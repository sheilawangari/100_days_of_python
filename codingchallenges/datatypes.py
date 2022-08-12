two_digit_number = input("Type a two digit number: ")

print(type(two_digit_number)) 

first_digit = two_digit_number[0]  # lets get the first digit number because of the index
second_digit = two_digit_number[1]  # the second digit 

result = int(first_digit) + int(second_digit)
print(result)