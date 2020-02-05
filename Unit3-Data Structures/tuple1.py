# Carter Costic
# tuple1.py

import random


def printLine(word):
    print("\n----" + word + "----\n")

# A function ‘printObj( obj )’ that will print any list/tuple passed
# as an argument


def printObj(obj):
    print(obj)


printLine("")
# A Tuple ‘numTuple’ that contains 4 numbers of your choice


numTuple = (1, 2, 3, 4)
# A Tuple ‘nameTuple’ that contains 4 names of your choice

nameTuple = ("Carter", "Carter", "Carter", "Carter")

# A list ‘numList’ that contains 4 numbers of your choice

numList = [1, 2, 3, 4]

# A list ‘nameList’ that contains 4 names of your choice

nameList = ["Carter", "Carter", "Carter", "Carter"]

# Using printObj(), print your two Tuples

printObj(numTuple)
printObj(nameTuple)
printLine("")
# Using printObj(), print your two Lists

printObj(numList)
printObj(nameList)
printLine("")
# Create print statements identifying the index of the third item in
# numTuple, nameTuple, numList and nameList

print(2)
print(2)
print(2)
print(2)
printLine("")

# Create print statements identifying the value of the second item in
# numTuple, nameTuple, numList and nameList

print(numTuple[2])
print(nameTuple[2])
print(numList[2])
print(nameList[2])
printLine("")

# Create a statement that checks to see if your numTuple contains the # number 30, and print the result

print(numTuple.__contains__(30))
printLine("")

# Create a statement that checks to see if your nameTuple contains
# ‘Mike’ and print the result

print(nameTuple.__contains__("Mike"))
printLine("")

# Create a statement that checks to see if your numList contains the
# number 30 and print the result

print(numList.__contains__(30))
printLine("")

# Create a statement that checks to see if your nameList contains your
# name and print the result

print(nameList.__contains__("Carter"))
printLine("")

# Part 2:

# Create objects that will store two of your lists/tuples, but in
# reverse. Print these objects using printObj()

parentObj1 = reversed(nameTuple)
parentObj2 = reversed(numTuple)
printObj(parentObj1)
printObj(parentObj2)
printLine("")

# Create objects that will store the other two of your lists/tuples,
# but sorted. Print these objects using printObj()

parentObj3 = sorted(nameTuple)
parentObj4 = sorted(numTuple)
printObj(parentObj3)
printObj(parentObj4)
printLine("")

# Create a tuple with 10 random numbers in it, from 1-4 inclusive.
# Using .count(), find out how many 3’s exist in this tuple, and print

numTuple2 = tuple([random.randint(1, 4) for i in range(10)])
print(numTuple2)
print(numTuple2.count(3))
printLine("")

# Turn nameTuple into a list newNameList using an abstract function

newNameList = list(nameTuple)

# Print newNameList reversed and sorted

newNameList = sorted(reversed(newNameList))
print(newNameList)
printLine("")

#
#
#

# Bonus 1

testTuple = (1, 2, 3, 4)


def tupleRemove(item, tuple1):
    tempList = list(testTuple)
    tempList.remove(item)
    newTuple = tuple(tempList)
    return newTuple


print(tupleRemove(3, testTuple))
printLine("")

# Bonus 2

testTuple1 = ("dog", "molotov", "halloween", "Indianapolis 500", "cool beans")
[print(value[::-1]) for value in list(testTuple1)]
