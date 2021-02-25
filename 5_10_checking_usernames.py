current_users = ['Admin', 'martha', 'helga', 'juliane', 'lena']
current_users_normalized = []

# Creating list of lower case names to compare to new usernames. 
for current_user in current_users:
	current_users_normalized.append(current_user.lower())


new_users = ['joe', 'Martha', 'hugo', 'jules', 'LENA']

for new_user in new_users:
	if new_user.lower() in current_users_normalized:
		print(f"Sorry, the username {new_user.title()} is already taken. Please enter a new username.")
	else:
		print(f"User {new_user.title()} is available.")	

