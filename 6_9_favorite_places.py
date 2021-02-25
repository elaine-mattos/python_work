favorite_places = {
	'mike' : ['johannisburg', 'berlin'],
	'maria' : ['rio', 'new york', 'tokyo'],
	'daniel' : ['upsalla', 'edinburg', 'valhalla'],
	'jose' : ['delhi'],
	'ludmilla' : [],
}

for name, fav_places in favorite_places.items():
	if (len(fav_places) > 1):
		print(f"{name.title()}'s favorite places are: ")
		for place in fav_places:
			print(f"\t{place.title()}")
	elif (len(fav_places) == 1):
		print(f"{name.title()}'s favorite place is: ")
		print(f"\t{fav_places[0].title()}")
		
	else:
		print(f"{name.title()} has no favorite places. ")