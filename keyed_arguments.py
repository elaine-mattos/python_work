def describe_pet(animal_type, pet_name):
	""" Display information about a pet. """
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type = 'hamster', pet_name=  'harry')

# There is no pb if you invert the order of the arguments...
describe_pet(pet_name=  'harry', animal_type = 'hamster')


