players = ['John', 'Ringo', 'Paul', 'George', 'Jagger', 'Hendrix', 'Baez']

print(f"This is the complete list {players}")
print(f"\nFrom index 1 to 3: {players[1:4]}")
print(f"\nFrom index 0 to 3: {players[:4]}")
print(f"\nFrom index 1 to the end: {players[1:]}")
print(f"\nReturns the second last item: {players[-2]}")
print(f"\nReturns the third last to last item: {players[-3:]}")
print(f"\nReturns itens in odd indexes: {players[1::2]}")

#You can also instance new lists from slices of other lists
sliced_players = players[::3]
print(f"\nThis is a new list, created from a slice: {sliced_players}")

#You can also loop through a slice
print("\nHere are the first 3 players on my list:")
for player in players[:3]:
	print(player.title())

