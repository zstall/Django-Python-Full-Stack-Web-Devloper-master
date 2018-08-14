# Lists
my_list = ['a', 'b', 'c', 'd', 'e']
my_list_two = ["string", 1, 2, 3, 4, 5, True, "abc", [1,2,3]]

print(len(my_list_two))
print(len(my_list))

print(my_list[-1])      # last item of the Lists
print(my_list[1:4])     # Can slice Lists

my_list[0] = "NEW"


print(my_list)

my_list.append("f")
print(my_list)


x = ['x', 'y', 'z']

my_list.extend(x)
print(my_list)

# vs

my_list_two.append(x)
print(my_list_two)

item = my_list.pop()

print(my_list)
print(item)

new_item = my_list.pop(0)
print(my_list)
print(new_item)

my_list.reverse()
print(my_list)

lst = [ 4,5,6,7,234,5,4,2]
lst.sort()
print(lst)

new_lst = [1,2,['x','y','z']]
print(new_lst[2][1])


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][0])

# List comprehension
first_col = [row[0] for row in matrix]
second_col = [row[1] for row in matrix]

print(first_col)
print(second_col)
