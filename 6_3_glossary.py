glossary = {
	'variables' : 'where you store values',
	'lists' : 'where you store sets of values',
	'if' : 'where you evaluate conditional statements',
	'for' : 'loops to execute repetitive stuff',
	'dictionaries' : 'this.',
}

print(f"Definitions")
for entry,definition in glossary.items():
	print(f"\n{entry.title()} : {definition.title()}")
