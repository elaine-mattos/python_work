# Please note that 'username' is a PARAMETER and 'jane doe' is an ARGUMENT.
def greet_user(username):
	# The comment below is a docstring: it's used to describe what the function does.
	# Python looks for these docstrings when it generates documentation fur the functions in your pgm.

	""" Display a simple greeting. """
	print(f"Hello, {username.title()}!")

greet_user('jane doe')
