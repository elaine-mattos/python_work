# You can nest a dict inside another dict, but your code can get
# too complicated quickly.

users = {
	'aeinstein' : {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
	},
	'mcurie':{
		'first' : 'marie',
		'last' : 'curie',
		'location' : 'paris',
	},

}

for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}".title()
	location = user_info['location'].title()

	print(f"\tFull name: {full_name}")
	print(f"\tLocation: {location}")