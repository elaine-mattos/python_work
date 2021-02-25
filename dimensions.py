#A tuple is an immutable list
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#we face an error if we try to modify the tuple
# dimensions[0] = 250
#"tuple object does not support item assigment"

#tuple with one element. You still need the comma
uni_dimensional_tuple = (3,)




print("Original dimensions: ")
#you can loop through them
for dimension in dimensions:
	print(dimension)

#writing over. Reassigning the whole tuple is a valid operation
dimensions = (400,100)
print("\nModified dimensions: ")
for dimension in dimensions:
	print(dimension)



