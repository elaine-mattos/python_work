person_1 = {
	'first_name' : 'alexia',
	'last_name' : 'parede',
	'age' : 50,
	'city' : 'santos',	
}

person_2 = {
	'first_name' : 'elaine',
	'last_name' : 'mattos',
	'age' : 42,
	'city' : 'rio de janeiro',	
}

person_3 = {
	'first_name' : 'camilla',
	'last_name' : 'borges',
	'age' : 12,
	'city' : 'minas gerais',	
}

people = [person_1, person_2, person_3]

for person in people:
	if len(people) > 0 :
		print(f"\nMeet {person['first_name'].title()}"
			  f" {person['last_name'].title()}."
			  f" {person['first_name'].title()} is {person['age']} years old."
			  f" {person['first_name'].title()} lives in {person['city'].title()}.")




