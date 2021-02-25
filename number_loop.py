#Prints numbers from 1 to 4!!!
for value in range(1,5):
	print(value)

print("\n")

#Prints numbers from 0 to 4
for value in range(5):
	print(value)

print("\n")

#Creates list of numbers between 1 and 5
numbers = list(range(1,6))
print(numbers)

#Creates list of odd numbers between 1 and 5. '2' is the step
odd_numbers = list(range(1,6,2))
print(odd_numbers)

#Creates a list of the first 10 square numbers
square_numbers = []
for value in range(1,11):
	square_numbers.append(value ** 2)
print(square_numbers)

print(f"\nMin: {min(square_numbers)}")
print(f"\nMax: {max(square_numbers)}")
print(f"\nSum: {sum(square_numbers)}")

