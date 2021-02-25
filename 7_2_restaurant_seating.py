number = input("How many people are in your group? ")
number = int(number)
if number > 8:
	print(f"\nSorry, but your {number}-people-group needs to wait for a table")
else:
	print(f"\nYour {number}-people-table is ready ")