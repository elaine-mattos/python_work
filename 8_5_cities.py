def describe_city(city, country = 'Brazil'):
	print(f"{city.title()} is in {country.title()}.")

describe_city('Rio de Janeiro')
describe_city('Los Angeles', 'the USA')
describe_city(city = 'Sao Paulo')