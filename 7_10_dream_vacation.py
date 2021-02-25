dream_vacation = {}
finished = False

while not finished:
	name = input("\nWhat is your name? ")
	place = input("\nIf yo could visit one place in the world, where would you go? ")
	dream_vacation[name] = place
	test = input("\nWould you like to let someone else answer to this poll? (yes/no)")
	if (test == 'no'):
		finished = True

# Polling is complete. SHow the results.
print("\n--- Poll Results ---")
for name, place in dream_vacation.items():
	print(f"{name.title()} would like to go to  {place.title()}")