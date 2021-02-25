sandwich_orders = ['american', 'bacon and cheese', 'italian', 'sweet chili']
finished_sandwiches = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(f"\nI made your {current_sandwich.title()} sandwich.")
	finished_sandwiches.append(current_sandwich)


print(f"\nAnd today we made the following sandwiches: ")
for finished_sandwich in finished_sandwiches:
	print(f"\t{finished_sandwich.title()}")