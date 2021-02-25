cities = {
	'paris' : {
		'country' : 'france',
		'population' : 100000, 
		'fact' : 'most visited in the world',
	},
	'london': {
		'country' : 'england',
		'population' : 200000,
		'fact' : 'home to the Big Ben',
	},
	'rio':{
		'country' : 'brazil',
		'population' : 320000,
		'fact': 'also known as the wonder city'
	},

}

for city, info in cities.items():
	print(f"Some of curiosities regarding {city.title()} are:") 
	print(f"\tCountry: {info['country'].title()}.")
	print(f"\tPopulation: {info['population']}.")
	print(f"\tFact: {info['fact'].title()}.\n")