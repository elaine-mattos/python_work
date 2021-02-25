
while True:
	topping = input("Please enter a topping for your pizza or enter 'quit' to stop: ")
	if topping.lower() == 'quit':
		break
	else:
		print(f"\nAdding {topping.title()}.")

