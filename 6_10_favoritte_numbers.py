fav_numbers = {
	'john' : [2, 3, 5, 2],
	'william' : [3],
	'bruna' : [5, 9, 10],
	'margret' : [19, 15, 22],
	'jacintha' : [13, 34],
}


for name, numbers in fav_numbers.items():
	if len(numbers) > 0:
		print(f"{name.title()}'s favorite numbers are: ")
		for number in set(numbers): # Using the set() function to remove duplicates
			print(f"\t{number}")