colors = ['green', 'yellow', 'red']
n = 0

for n in [0,1,2]:
	alien_color = colors[n]
	if (alien_color == 'yellow' or alien_color == 'red'):
		print("You just earned 10 points!")
	else:
		print("You just earned 5 points!")
	n = n + 1

