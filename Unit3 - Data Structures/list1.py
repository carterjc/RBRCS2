nameList = ["Carter", "Carter", "Carter", "Carter"]  # I'm not egotistical, I swear

for name in nameList:
    print(name)

print("\n")

print(nameList[2])
print(len(nameList))

print("\n")


def printList():
    for name in nameList:
        print(name)


nameList.extend(nameList[:3])
printList()
print("\n")

nameList.remove("Carter")
nameList.remove("Carter")
printList()
print("\n")

nameList[0] = "Carterx"
printList()
print("\n")

del nameList[-1]
printList()
print("\n")


def printMessage():
    specialString = ""
    for name in nameList:
        specialString += name + ", "
    print("Hi, " + specialString[:-2])


printMessage()


# Bonus

myList = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]


def shiftByX(x):
    newList = []
    startingIndex = (len(myList) - x) % len(myList)
    for i in range(startingIndex, len(myList)):
        newList.append(myList[i])
    newList.extend(myList[:startingIndex])
    print(newList)


shiftByX(1)


def shiftByX2(x):
    newList = []
    newList.extend(myList[(len(myList) - x) % len(myList):])
    newList.extend(myList[:(len(myList) - x) % len(myList)])
    print(newList)


shiftByX2(1)


def shiftByX3(x):
    for i in range(x % len(myList)):
        myList.insert(0, myList.pop())
    print(myList)


shiftByX3(1)
