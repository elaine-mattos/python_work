rivers = {
	'Nile' : 'Egypt',
	'hudson' : 'USA',
	'Amazon' : 'Brazil',
	'Maracana' : 'Brazil',
	'Spree' : 'Germany',
	'Main' : 'Germany',
}

for river, country in rivers.items():
	print (f"The {river.title()} runs in {country.title()}.")

print('\n')

for river in set(rivers.keys()):
	print(f"This river was mentioned at least once: {river.title()}")

print('\n')

for country in set(rivers.values()):
	print(f"This country was mentioned at least once: {country.title()}")

