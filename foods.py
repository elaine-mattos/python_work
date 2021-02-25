#Create a NEW list based on the first
my_foods=['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

print("\n-------------------------------------\n")

#proving they are different lists
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

print("\n-------------------------------------\n")

#Creating the same list (just like a pointer)
my_foods=['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)

print("\nMy friends favorite foods are: ")
print(friend_foods)

