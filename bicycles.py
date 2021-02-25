transport = ['bus', 'train', 'bike', 'skate']
print(f"Printing list: {transport}")
print(f"Printing first element: {transport[0].title()}")
print(f"Printing second element: {transport[1].title()}")
print(f"Printing third element: {transport[-2].title()}")
print(f"Printing last element: {transport[-1].title()}")

#changing elements
transport[0] = 'tram'
print(transport)

#appending elements
transport.append('bus')
print(transport)

#inserting elements
transport.insert(2,'tuk-tuk')
print(transport)

#removing elements
del transport[2]
print(transport)


#popping elements
print("\n\n----------------------------------------------------------------\n\n")
#chronologically ordered list of motorcycles I owned
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
first_owned = motorcycles.pop(0)

print(f"The last motorcycle I owned was a {last_owned.title()}.")

print(f"The first motorcycle I owned was a {first_owned.title()}.")


#removing elements by value
print("\n\n----------------------------------------------------------------\n\n")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(f"The new list is: {motorcycles}")

too_expensive = 'ducati'
motorcycles.append(too_expensive)
print(f"The new list has Ducati again: {motorcycles}")

motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")