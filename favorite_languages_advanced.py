# It's good practice to add a comma at the end
favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python',
}

# Looping through the dictionary, based on key and value
for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")

print('\n')

# Looping through the dict, based on key only
# for name in favorite_languages.keys(): 
# Using the 'keys()' method is optional
for name in favorite_languages:
	print(name.title())

print('\n')

friends = [ 'jen', 'phil']
for name in favorite_languages.keys():
	print(f"Hi {name.title()}.")

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")


if 'erin' not in favorite_languages.keys():
	print("\nErin, please take our poll! It's fun!")

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")	


# Looping through all VALUES in a dict
print("\nThe following languages have been mentioned: ")
for language in favorite_languages.values():
	print(language.title())	


# To avoid repetition use the 'set()' method. 
# A set is a collection in which each item must be unique
print("\nThe following languages have been mentioned at least once: ")
for language in set(favorite_languages.values()):
	print(language.title())	

