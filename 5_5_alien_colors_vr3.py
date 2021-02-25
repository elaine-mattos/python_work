colors = ['green', 'yellow', 'red']
n = 0

for n in [0,1,2]:
	alien_color = colors[n]
	if (alien_color == 'green'):
		print("You've just earned 5 points")
	elif (alien_color == 'yellow'):
		print("You've just earned 10 points")
	elif (alien_color == 'red'):
		print("You've just earned 15 points")
	n = n + 1