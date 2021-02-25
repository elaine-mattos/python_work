while True:
	age = input("How old are you? Hit '0' to quit program. ")
	age = int(age)

	if (age == 0 ):
		break

	if (age  > 0 and age < 3):
		print("Your ticket is free. ")
	if (age >=3 and age <= 12 ):
		print("You pay 10USD. ")
	if (age > 12):
		print("You pay 15USD.")


