sandwich_orders = ['american', 'pastrami', 'bacon and cheese', 'pastrami', 'italian', 'sweet chili', 'pastrami']
finished_sandwiches = []

print("Unfortunately we have run out of Pastrami.")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
	
while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(f"\nI made your {current_sandwich.title()} sandwich.")
	finished_sandwiches.append(current_sandwich)


print(f"\nAnd today we made the following sandwiches: ")
for finished_sandwich in finished_sandwiches:
	print(f"\t{finished_sandwich.title()}")