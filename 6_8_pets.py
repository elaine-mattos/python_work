pet_1 = {
	'kind': 'dog',
	'owner' : 'jake', 
}

pet_2 = {
	'kind': 'cat',
	'owner' : 'jill', 
}

pet_3 = {
	'kind': 'parrot',
	'owner' : 'john', 
}

pet_4 = {
	'kind': 'turtle',
	'owner' : 'johanna', 
}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
	print(f"{pet['owner'].title()} owns a {pet['kind']}.")