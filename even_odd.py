number = input("Enter a number, and I'll tell you if it's odd or even: ")
number = int(number)

if (number % 2 ) == 0:
	print(f"\nThe number {number} is even.")
else:
	print(f"\nThe number {number} is odd.")