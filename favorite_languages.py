# It's good practice to add a comma at the end
favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# Using the get() method to avoid errors calling a non-existing key
language = favorite_languages.get('jane', 'This user is not on the list.')
print(language)

