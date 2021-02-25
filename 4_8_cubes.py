cubes = []
for value in range(1,11):
	cubes.append(value **3)
print(f"This is the hard way of creating a list{cubes}")


cubes = [value **3 for value in range(1,11)]
for value in cubes:
	print(f"\n{value}")