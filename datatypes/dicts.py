# FriendFace post

post = {"user_id": 209, "message": "Hello World", "language": "English",
        "datetime": "20230215T124231Z", "location": (44.590533, -104.715556)}
print("The first dictionary contains:")
print(post, "\n")

# Inputs are keys, outputs are values
# There are a number of data types for the keys
# user_id = Integer
# message = string
# language = string
# datetime = string
# location = a tuple of floats

# We can also use the "dict" constructor to create a dictionary

post2 = dict(message="SS Cotopaxi", language="English")
print("The second dictionary contains:")
print(post2, "\n")

# add additional values.
print("Adding more values to the dictionary...", "\n")
post2["user_id"] = 209
post2["datetime"] = "19771116T093001Z"
# note that the key names do not need "" when using the dict constructor, but they do when used with []
print("Now the second dictionary contains:")
print(post2, "\n")

# Now to print the values of specific keys in the dictionary "post"
print("The value for the key 'message' in the dictionary 'post' is:")
print(post['message'])

# Try to print the key for a value in a dictionary when it does not have a value.
# This will normally end in a KeyError.
# AYou can avoid using 'if' and 'in'
if 'location' in post2:
    print(post2['location'])
else:
    print("The dictionary 'post2' does not have a value for the key 'location'.")

# Or a better way is using proper error handling.

try:
    print(post2['location'])
except KeyError:
    print("The dictionary 'post2' does not have a value for the key 'location'.")
