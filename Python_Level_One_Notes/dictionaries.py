# Dictionaries
my_stuff = {"key1" : "value", "key2" : "value2", "key3":{"123":[1,2,"grabMe"]}}

print(my_stuff)
print(my_stuff["key2"])
# pulling a nested element from a list in a key value pair nested in a dictionary
print(my_stuff["key3"]["123"][2])
print(my_stuff["key3"]["123"][2].upper())

food = {'lunch':'pizza', 'bfast':'eggs'}
print(food['lunch'])


# Changing a value for a key
food['lunch'] = 'burger'
print(food['lunch'])


# adding a key value pair
food['dinner'] = 'pasta'
print(food)
