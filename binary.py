# Import math module
import math

#Create user prompt to input a binary number:
binary_input = list(input("Input a binary number: "))
value = 0

#Create a loop to calculate the users input and convert it to a decimal:
for i in range(len(binary_input)):
	digit = binary_input.pop()
	if digit == '1':
		value = value + pow(2, i)

#Print the corresponding integer value:
print("The decimal value of the number is", value)
