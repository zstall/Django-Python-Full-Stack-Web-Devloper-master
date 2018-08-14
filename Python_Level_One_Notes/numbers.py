
# when creating a var in python, you do not need to declare types
my_income = 60000
tax_rate = 0.1

# Even when adding two different types (int and float) python will add and make answer a float
my_taxes = my_income * tax_rate

print(my_taxes)

# STRINGS

# Basics
# Can use single or double quotations
'hello'
"hello"
# can use a single inside a double
" I'm a dog "

my_string = 'abcdefg'
print(my_string)
print(my_string[0])     # first letter
print(my_string[-1])    # last letter
print(my_string[3])     # 'd' fourst letter


# SLICING
print(my_string[2:])    # starting at c go to the end = abcdefg
print(my_string[4:])    # starting at e go to the end = efg
print(my_string[:3])    # starting at index 0, go up to but not including index = abc
print(my_string[2:5])   # Starting at 2 and go up to before 5 = cde
print(my_string[::2])   # step size,  will return every other letterself.

# Strings are immutable, meaning I can not reasign a index like my_string[2] = "x". This will cause an error

x = my_string.upper()   # this makese everything upper cause
print(x)

y = my_string.lower()
print(y)

new_string = "hello world"
z = new_string.split()
print(z)

m = new_string.split('e')
print(m)


n = "insert one: {e} Insert two: {f}".format(e = "dog", f = "cat")
print(n)
