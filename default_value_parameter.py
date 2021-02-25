# Note that the default-valued parameter has to be defined AFTER the regular parameter
def describe_pet(pet_name, animal_type = 'dog'):
	""" Display information about a pet. """
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')
describe_pet('Diogo')