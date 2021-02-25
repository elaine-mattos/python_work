requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
#requested_toppings = []


# When the name of a list is used in an if statement, Python returns 
# True if the list is not empty
if requested_toppings:
	for requested_topping in requested_toppings:
		if requested_topping == 'green peppers':
			print("Sorry, we're out of green peppers today")
		else:
			print(f"Adding {requested_topping}.")
	print("\nFinished making your pizza!")

else:
	print("Are you sure you want a plain pizza?")

