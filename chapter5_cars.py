cars = ['audi', 'bmw', 'subaru', 'toyota']


#Allowed expressions are:
# == equal
# != not equal
# > more than
# < less than
# <= less than or equal to 
# >= more than or equal to
# and, or, in, not in


for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())


