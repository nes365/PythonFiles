# Sets tutorial
# Create a set
example = set()

# Populate a set
example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")

# Print all elements of the set.
print("Here is an example set:")
print(example)
print("The number of elements in the set is: ", len(example), "\n")
# Note that the set does not have an order.

# Adding elements to the set which already exist
print("Adding an the element \"42\" which already exists:")
example.add(42)
print(example)
print("The number of elements in the set is still: ", len(example), "\n")
# The set stil contains one copy of the element 42. Sets do not contain duplicate elements.

# Removing an element from the set.
example.remove(42)
print("Removing the element \"42\" from the set")
print(example)
print("The number of elements in the set is now: ", len(example), "\n")
# If you try and remove an element which does not exist in the set then you will get a KeyError.
# Alternatively, use the discard method to remove an element from the set.
# If the element does not exist in the set then "discard" will silently fail.


# Creating and populating a set in one line
example2 = set([28, True, 2.71828, "Helium"])
print("Here is the second example set, created in one line:")
print(example2)
print("The number of elements in this set is:", len(example2), "\n")

# To clear a set in one go, use the "clear" method
example2.clear()
print("Here is the second example set, after using the \"clear\" method:")
print(example2)
print("The number of elements in this set is now:", len(example2), "\n")
