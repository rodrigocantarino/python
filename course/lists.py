"""

Lists

Lists in Python work as arrays in other programming languages, it is dynamic and nay have any data type inside.


"""


list1 = []
list2 = [1, 7, 5, 65, 48, 5, 20, 54, 99, 1, 2, 5]
list3 = ["R", "o", "d", "r", "i", "g", "o"]
list4 = list(range(11))
list5 = list("Rodrigo Cantarino")
list6 = [list1, list2, list3, list4, list5]
list7 = ["bla", "blabla", "blablabla"]

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)

print(type(list1))
print(type(list2))
print(type(list3))
print(type(list4))
print(type(list5))
print(type(list6))

# Check if a values is inside the list
search_value = 99
if search_value in list2:
    print(f"{search_value} found")
else:
    print(f"{search_value} not found")

search_value = 'd'
if search_value in list3:
    print(f"Letter '{search_value}' found")
else:
    print(f"Letter '{search_value}' not found")

search_value = 12
if search_value in list4:
    print(f"{search_value} found")
else:
    print(f"{search_value} not found")

search_value = 'Rodrigo'
if search_value in list5:
    print(f"{search_value} found")
else:
    print(f"{search_value} not found")

search_value = list5
if search_value in list6:
    print("list5 found")
else:
    print("list5 not found")

search_value = list7
if search_value in list6:
    print("list7 found")
else:
    print("list7 not found")

#  Sort items
list2.sort()
print(list2)

#  Count how many times a value occurs
print('_________________________________________________')
print(f'The number "5" occurs {list2.count(5)} times!')
print(f'The letter "R" occurs {list5.count("R")} times!')
print(f'The letter "r" occurs {list5.count("r")} times!')
print('_________________________________________________')

#  Add new elements using the 'append' method (by default, the value is added at the end of the list)
#  The 'append' method takes exactly 'ONE' argument, nothing more
print("Add new elements using the 'append' method")
print(list2)
#  Right way
list2.append(100)
#  Wrong way
#  list2.append(100, 5, 3)
print(list2)
print('_________________________________________________')

#  Add new elements using the 'extend' method (by default, the value is added at the end of the list)
#  The 'extend' method takes as argument an iterable value
print("Add new elements using the 'extend' method ")
print(list2)
list2.extend([55, 33, 22, 88])
print(list2)
print('_________________________________________________')
#  Add new elements using the 'insert' method
#  Doc: Insert object before index.
#  The 'insert' method takes as argument the index and an object
print("Add new elements using the 'insert' method")
list2.insert(2, 1985)
print(list2)
print('_________________________________________________')

#  Join two or more lists. Use '+'
print("Join two or more lists. Use '+'")
list_join = list2 + list3
print(list_join)
print('_________________________________________________')

#  Reverse a list
print("Reverse a list")
print(list_join[::-1])
#  Or
list_join.reverse()
print(list_join)
print('_________________________________________________')

#  Copy a list
print("Copy a list")
list_join.reverse()
list_join_copy = list_join
print(list_join_copy)
print('_________________________________________________')

#  List Length
print("List Length")
print(len(list1))
print(len(list2))
print(len(list_join_copy))
print('_________________________________________________')

#  Remove an element of a list using 'pop' (by default, the element removed is the last element of the list)
#  Doc: Remove and return item at index (default last).
#       Raises IndexError if list is empty or index is out of range.
print("Remove the last element of a list (list2)")
print(list2)
returned_removed_value = list2.pop()
print(list2)
print("returned_removed_value")
print(returned_removed_value)
print("(list2)")
print(list2)
returned_removed_value_index = list2.pop(2)
print("returned_removed_value_index")
print(returned_removed_value_index)
print('_________________________________________________')

#  Clear list
print("Clear list (list_join)")
print(list_join)
list_join.clear()
print(list_join)
print('_________________________________________________')

#  Repeat elements inside a list
print("Repeat elements inside a list")
repeated_list = list3 * 3
print(repeated_list)
print('_________________________________________________')

#  Ways to convert strings on lists
#  First way
string_to_convert = "Rodrigo Pessoa Cantarino de Oliveira"
print(f'string_to_convert: {string_to_convert}')
print("string_to_convert first way: ")
list_from_str1 = string_to_convert.split() # By default, the separator is the ' ' (space char)
print(list_from_str1)
#  Second way
print("string_to_convert second way: ")
list_from_str2 = list(string_to_convert)
print(list_from_str2)
print('_________________________________________________')

# Convert a list to a string
print("Convert a list to a string")
name = ' '.join(list_from_str1)
print('Name: ' + name)
name2 = '_'.join(list_from_str1)
print('Name2: ' + name2)
print('_________________________________________________')

#  Iteration
for el in list6:
    print(el)

#  Using variables inside a list
print("Using variables inside a list: list6 = [list1, list2, list3, list4, list5]")
list6 = [list1, list2, list3, list4, list5]
print(list6)
print('_________________________________________________')

colours = ['green', 'yellow', 'blue', 'white']

for colour in colours:
    print(colour)

print('_________________________________________________')

index = 0
while index < len(colours):
    print(colours[index])
    index += 1

print('_________________________________________________')

#  Generating a index inside a 'for' structure

for index, colour in enumerate(colours):
    print(index, colour)

print('_________________________________________________')

#  How to find a element index?
#  list2 = [1, 7, 5, 65, 48, 5, 20, 54, 99, 1, 2, 5]
print(list2.index(48))
print(list2.index(99))
# When the element is repeated, the index returned will be from the first element founded
print(list2.index(5))
# Starting from a specific position. If there is no value from that position, the Python will throw a valueError
print(list2.index(5, 3))

# Between a specific positions. If there is no value from that position, the Python will throw a valueError
print(list2.index(5, 3, 7))

print('_________________________________________________')

# Slice list[begin, end, pass]
print(list2)
print(list2[0])
print(list2[1::])
print(list2[1:4:])
print(list2[1:6:2])
print(list2[:6])
print(list2[::-1])
print('_________________________________________________')

#  Sum, max value, min value
#  For integer or float elements inside a list
#  And list length
print('sum(list2)')
print(sum(list2))
print('max(list2)')
print(max(list2))
print('min(list2)')
print(min(list2))
print('len(list2)')
print(len(list2))
print('_________________________________________________')

#  Convert list on tuple
print('Convert list on tuple')
tuple_from_list = tuple(list2)
print(tuple_from_list)
print('_________________________________________________')

#  List unpack
#  list7 = ["bla", "blabla", "blablabla"]
print('List unpack')
v1, v2, v3 = list7
print(list7)
print(v1)
print(v2)
print(v3)
print('_________________________________________________')

#  Copy list, shallow copy and deep copy

new_list = list7.copy()
# Deep copy
new_list.append('blablablabla')  # this append doesn't affect the original list
print(list7)
print(new_list)

# Shallow copy -
new_list = list7
new_list.append('blablablabla')  # this append affect the original list
print(list7)
print(new_list)
