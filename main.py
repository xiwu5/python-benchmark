# Beneath each comment write the code and print out the result to check it works

'''LISTS'''

# Create a list and assign it to a variable
my_list = [3, 1, 4, 1, 5, 9, 2]

# Find the length of the list
print(len(my_list))

# Append an item to the list
my_list.append(6)

# Find the value of an item in the list a specific index
print(my_list[2])

# Set the value of an item at a specific index
my_list[0] = 10

# Check whether an item is in the list
print(5 in my_list)

# Sort the list
my_list.sort()

# Iterate over the list using range, printing out each element and the index
for i in range(len(my_list)):

# Iterate over the list without using range, printing out each element
    for item in my_list:
        print(i, my_list[i])
        i += 1

        print(item)
'''TUPLES'''

# Create a tuple and assign it to a variable
my_tuple = (3, 1, 4, 1, 5, 9, 2)

# Find the length of the tuple
print(len(my_tuple))

# Find the value of an item in the tuple a specific index
print(my_tuple[2])

# Check whether an item is in the tuple
print(5 in my_tuple)

# Iterate over the tuple using range, printing out each element and the index
for i in range(len(my_tuple)):
    print(i, my_tuple[i])

# Iterate over the tuple without using range, printing out each element

'''STRINGS'''

# Create a string and assign it to a variable

# Find the length of the string
my_string = "Hello, World!"
print(len(my_string))

# Find the value of an character in the string a specific index

# Check whether an item is in the string

# Concatenate (add) two strings together
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
# Create an f-string
f_string = f"{greeting}, {name}!"
# Split a string using .split
words = my_string.split(", ")
# Join a list of strings using .join
joined_string = " ".join(words)
# Iterate over the string using range, printing out each character and the index

# Iterate over the string without using range, printing out each character

'''DICTIONARIES'''

# Create a dictionary and assign it to a variable

# Find the length of the dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(len(my_dict))
# Add a new key/value pair

# Replace value for a given key

# Check whether a key is in the dictionary

# Iterate over keys, printing each key

# Iterate over over key/value pairs using .items(), printing each key and value

'''SETS'''

# Create a set and assign it to a variable

# Find the length of the set

# Add a new element

# Remove an element

# Check whether a element is in the set

# Iterate over elements, printing each one out

'''NUMBERS'''

# Add / subtract / multiply 2 numbers

# Divide two numbers using normal (float) division

# Divide two numbers using integer division

# Find the modulo (remainder) of two numbers

# Check whether a number is even/odd

# Round a float down to an int


'''FUNCTIONS'''

# Write a function that takes no arguments and call it

# Write a function that takes one or more arguments and call it

# Write a function that returns a value. Call the function and store the return value in a variable

'''LOOPS'''

# Write a while loop

# Write a for loop that loops a set number of times (e.g. 10 times)

'''CONDITIONALS'''

# Write an if/elif/else statement

# Write conditionals for the following operators:
# ==
# !=
# <
# >
# <=
# >=

'''NESTED DATA'''

# Write a nested list (a list of lists) and assign it to a variable

# Print an item at a specific position in the data structure (e.g. the item at a given row and column). HINT: row comes first, column comes second

# Iterate through the nested data structure using range

# Iterate through the nested data structure without using range 

'''REMINDER'''

# You're doing great and you got this!
