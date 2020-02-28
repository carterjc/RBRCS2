# Carter Costic
# list2.py

numList = [1, 2, 3, 4]


def printList(list):
    for thing in list:
        print(thing)


printList(numList)

print("\n")

numList.extend([1, 2, 3, 4, 5])
printList(numList)

print("\n")

del numList[0:2]
printList(numList)

print("\n")


def addFive(list):
    for i in range(len(list)):
        list[i] = list[i] + 5


addFive(numList)
printList(numList)

print("\n")


def multiList(list):
    product = 1
    for i in list:
        product *= i
    return product


def minNum(list):
    min_num = list[0]
    for i in list:
        if i < min_num:
            min_num = i
    return min_num
# or return min(list)


def maxNum(list):
    max_num = list[0]
    for i in list:
        if i > max_num:
            max_num = i
    return max_num
# or return max(list)


print(minNum(numList))

print("\n")


#
#
#

myList = [5000, 1000000000000, 400000000000, 400]


def addCommasSingle(num):
    commaCounter = 1
    num = str(num)
    newNum = ""
    for i in range(len(num) - 1, -1, -1):  # start at the last index, go to 0 (stop is exclusive, by -1
        if commaCounter % 3 == 0 and i != 0:
            newNum += num[i] + ','
        else:
            newNum += num[i]
        commaCounter += 1
    return newNum[::-1]


def addCommas(list):
    for i in range(len(list)):
        list[i] = addCommasSingle(list[i])
    return list


myNewList = addCommas(myList)
for i in myNewList:
    print(i)
