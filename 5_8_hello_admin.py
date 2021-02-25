user_names = ['Elaine', 'john', 'adMin', 'barbara', 'helga']

for user_name in user_names:
	if (user_name.lower() == 'admin'):
		print("Hello Admin, would you like to see a status report?")
	else:
		print(f"\nHello {user_name.title()}. Thank you for logging in again!")

