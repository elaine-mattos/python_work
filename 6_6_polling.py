fav_language ={
	'alison': 'java',
	'jordan' : 'java',
	'johanna' : 'c',
	'william' : 'python',
	'camilla' : 'matlab',
}

employees = ['alison', 'jordan', 'bill', 'johan', 'johanna']

for employee in employees:
	if employee in fav_language.keys():
		print(f"Hi {employee.title()}, thank you for responding our poll")
	else:
		print(f"{employee.title()}, please take part in our poll")