prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end program. "

active = True
while active:
	message = input(prompt)
	
	if (message == 'quit'):
		print("Game over!")
		active = False
	else:
		print(message)
