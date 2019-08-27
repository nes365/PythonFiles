# Organising Lists

# Create a new list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is a list of cars.")
print(cars, '\n')
# Sort the list permenantly
cars.sort()  # This permenantly changes the order (alphabetic order)
print("Here is the same list of cars permenantly sorted alphabetically.")
print(cars, '\n')

cars.sort(reverse=True)  # Sorts in reverse
print("Here is the same list of cars permenantly sorted reverse alphabetically.")
print(cars, '\n')

# Sorting a list temporarily
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list.")
print(cars, '\n')
print("Here the list temporarily sorted alphabetically.")
print(sorted(cars), '\n')
print("Here is the original list back to normal")
print(cars, '\n')
