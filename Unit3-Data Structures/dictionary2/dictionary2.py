# Carter Costic
# dictionary2.py

import random

# Part 1:
# Create a dictionary ‘class_roster’
# Supply class_roster with 5 entries that follow the format below:
#
# 	{ ‘name’: ‘Matthew’, ‘age’: 15, ‘favSubject’: ‘Math’ }
# 	{ ‘name’: ‘Jessica’, ‘age’: 15, ‘favSubject’: ‘English’ }

class_roster = {
    0: {
        'name': 'Matthew',
        'age': 15,
        'favSubject': 'Math'
    },
    1: {
        'name': 'Edwin',
        'age': 15,
        'favSubject': 'Math'
    },
    2: {
        'name': 'Yaqub',
        'age': 15,
        'favSubject': 'Science'
    },
    3: {
        'name': 'Yvette',
        'age': 15,
        'favSubject': 'Science'
    },
    4: {
        'name': 'Willa',
        'age': 16,
        'favSubject': 'Math'
    }
}

# Print the first element of class_roster
print(class_roster[0])

print("\n-----\n")

# Print only the name of the first element of class_rosters
print(class_roster[0]['name'])

# Print each item of the dictionary using .format()
for key, value in class_roster.items():
    print("\n-----\n")
    for key1, value1 in class_roster[key].items():
        print("{}: {}".format(key1, value1))

print("\n-----\n")

# Create a function ‘printClassRoster’ to print class_roster


def printClassRoster():
    for key, value in class_roster.items():
        print("\n-----\n")
        for key1, value1 in class_roster[key].items():
            print("{}: {}".format(key1, value1))


# Change the first students’ favorite subject to ‘Computer Science’

class_roster[0]['favSubject'] = 'Computer Science'

# printClassRoster()

printClassRoster()

print("\n-----\n")

# Increase Edwin’s age by 1 and printClassRoster()

class_roster[1]['age'] += 1
printClassRoster()

print("\n-----\n")

# Add a ‘totalClasses’ key to each object, set it to 5

for key, value in class_roster.items():
    class_roster[key]['totalClasses'] = 5

# Update printClassRoster() to handle totalClasses

# printClassRoster()

printClassRoster()

print("\n-----\n")

# Part 2:

# Add a LIST of subjects under the key ‘subjectList’, include various # subjects of your choice

subjectList = ["Math", "Computer Science", "English", "Science", "History", "Networking", "Gym"]

# Update ‘totalClasses’ to provide a more accurate total per student
# based on subjectList

for key, value in class_roster.items():
    start = random.randint(0, 2)
    end = random.randint(start + 1, len(subjectList))
    class_roster[key]['subjectList'] = subjectList[start:end]

for key, value in class_roster.items():
    class_roster[key]['totalClasses'] = len(class_roster[key]['subjectList'])

# printClassRoster()

printClassRoster()
