available_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'olives', 'pepperoni', 'pineapple']
requested_toppings = ['mushrooms', 'green peppers', 'bananas']
#requested_toppings = []

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping} at the moment.")

print("\nFinished making your pizza.")
