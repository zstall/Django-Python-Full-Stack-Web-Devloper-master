# Booleans
True
False

# Tuples - immutable sequences
t = (1,2,3)
print(t[0])

t = ('a', True, 123)
# t[0]="new" - This will throw an error because tuples are immutable
print(t)


# sets - unordered set, looks like a dictionary, but no key value pairs
# only takes unique elements
x = set()
x.add(1)
x.add(2)
x.add(3)
x.add(4)
x.add(4)
x.add(4)

print(x)  # will only have one four

l = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,4,6,6,6,6,6,6]
converted = set(l)
print(converted)
