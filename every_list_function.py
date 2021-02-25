names = ['elza', 'anna', 'christoph', 'hans', 'olaf']
print(f"\nThis is my list {names}.")

names_count = len(names)
print(f"\nThere are {names_count} names in the list.")

names.reverse()
print(f"\nThis is the plain reversed list {names}.")
#unreverse
names.reverse()

names.sort()
print(f"\nThis is the sorted list {names}.")

names.sort(reverse=True)
print(f"\nThis is the sorted reversed list {names}.")

names_sorted = sorted(names)
print(f"\nThis is a temporarily sorted list {names_sorted}")

names_rsorted = sorted(names, reverse=True)
print(f"\nThis is a temporarily reversed list {names_rsorted}")

names_remove_last_item = names.pop()
print(f"\nRemoved last added item {names_remove_last_item.title()}. The new list is: {names}")

names_remove_first_item = names.pop(0)
print(f"\nRemoved first item {names_remove_first_item.title()}. The new list is: {names}")

names.remove('elza')
print(f"\nRemoved item 'Elza' {names}")

del names[1]
print(f"\nRemoved item 2. The list is now:  {names}.")


names.insert(0,'mom')
print(f"\nAdded item to 1st position. {names}.")

names.append('dad')
print(f"\nAdded item to last position {names}.")

names[1] = 'of the southern isles'
print(f"\nChanged prince Hans' name to: {names[1].title()}.")
