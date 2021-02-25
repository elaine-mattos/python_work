# ATTENTION: due to the input() function this program 
# will only run from the command line
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name.title()}!")

height = input(f"How tall are you {name.title()}, in inches? ")
height = int(height)

if (height >= 48):
	print(f"\nHey {name.title()}, you're tall enough to ride!")
else:
	print(f"\nSorry {name.title()}, you'll be able to ride when you're a little older.")
