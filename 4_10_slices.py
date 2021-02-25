import math

my_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
print("\nThe first three items in the lilst are: ")
print(my_list[:3])

print("\nThree items from the middle of the list are: ")
middle_of_list = math.floor(len(my_list) / 2)
print(my_list[(middle_of_list - 1): (middle_of_list + 2)])

print("\nThe last three items in the lilst are: ")
print(my_list[-3:])