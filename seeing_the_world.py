places = ['Annecy', 'Carcassonne', 'Lyon', "Côte d'Azur", 'Venice']
print(f"\nHere's the list of places I'd like to visit: {places}")

print(f"\nHere's the list in alphabetical order {sorted(places)}")
print(f"\nMy list is still unordered {places}")
print(f"\nHere's the list in reverse order {sorted(places, reverse=True)}")
print(f"\nMy list is still unordered {places}")

# Sorting permanently
places.sort()
print(f"\nHere's the permanently sorted list {places}")

# Reversing permanently
places.sort(reverse=True)
print(f"\nHere's the permanently reversed list {places}")

