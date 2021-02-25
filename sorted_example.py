cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

sorted_cars = sorted(cars)
reverse_cars = sorted(cars,reverse=True)
print("\nHere is the sorted list:")
print(sorted_cars)
print("\nHere is the reverse sorted list:")
print(reverse_cars)
print("\nHere is the original list again:")
print(cars)

#Print in reverse order (not sorted, just reverse). 
#The change is also PERMANENT
cars.reverse()
print(f"\nHere is the reversed list {cars}.")


#Length
car_list_length = len(cars)
print(f"\nThe car list has {car_list_length} elements.")


