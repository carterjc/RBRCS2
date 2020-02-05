# Part 1
# Create a dictionary ‘colorInt’ with ascending integers as keys
# beginning at zero and five of your favorite colors as values

colorInt = {
    0: 'blue',
    1: 'turquoise',
    2: 'aqua',
    3: 'cyan',
    4: 'navy',
    5: 'electric'
}

# Print this dictionary using a for loop (try using .format!())
for key, value in colorInt.items():
    print("{}: My favorite color is {}.".format(key, value))

print("\n-----\n")

# Create another dictionary ‘colorString’ with strings as keys, and
# colors as values. The keys shall be the first letter of the color.
# please stick to primary and secondary colors to avoid key confusion

colorString = {
    'b': 'blue',
    't': 'turquoise',
    'a': 'aqua',
    'c': 'cyan',
    'n': 'navy',
    'e': 'electric'
}

# Print this dictionary using a for loop

for key, value in colorString.items():
    print(key + ": " + value)

print("\n-----\n")


# Part 2:
# Create a function ‘printDictionary’ that takes in a dictionary as a
# parameter and prints it


def printDictionary(dict):
    for key, value in dict.items():
        print(str(key) + ": " + str(value))


# Print a value inside both dictionaries by searching for a key


print(colorInt[0])
print(colorString['b'])

print("\n-----\n")

# Print the length of both dictionaries

print(len(colorInt))
print(len(colorString))

print("\n-----\n")

# Add three more colors to colorInt and print

colorInt[6] = "azure"
colorInt[7] = "stone"
colorInt[8] = "aegean"
printDictionary(colorInt)

print("\n-----\n")

# Delete one key/value pair of colorInt and print
del colorInt[8]
printDictionary(colorInt)

print("\n-----\n")

# Change one of the values using .update()
colorInt.update({7: 'peacock'})
printDictionary(colorInt)

print("\n-----\n")

# Part 3:
# Create a function that takes in two parameters (dictionary,
# search_value)


def randFunc(dict, search_value):
    inDict = False
    for key, value in dict.items():
        if value == search_value:
            inDict = True
    if inDict:
        print("It's true - '{}' is in the dictionary.".format(search_value))
    else:
        print("Horrible. Terrible. Disgusting. '{}' is not in the dictionary.".format(search_value))


# Print a formatted statement if the search_value is found inside the # dictionary or an error
# message if no result is found

randFunc(colorInt, "peacock")
randFunc(colorInt, "peacok")
