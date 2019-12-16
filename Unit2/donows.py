def donow2(num):
    return num ** 3 if num > 5 else num ** 2 if num < 5 else 2.5

print(donow2(5))
print(donow2(6))
print(donow2(4))


# 4/Oct/19

def newSentence():
    print("Bob said, '" + str(input("Enter four words") + "'."))


def newSentence2():
    userInput = str(input("Enter four words"))
    spaceIndices = []
    for i in range(len(userInput)):
        if userInput[i] == " ":
            spaceIndices.append(i)
    print("This is the sentence: " + userInput[:spaceIndices[0]] + ", " + userInput[spaceIndices[0]+1:spaceIndices[1]] + ", " + userInput[spaceIndices[1]+1:spaceIndices[2]] + ", " + userInput[spaceIndices[2]+1:] + ".")


def newSentence3(userInput):
    spaceIndices = [i for i in range(len(userInput)) if userInput[i] == " "]
    print("This is the sentence: " + userInput[:spaceIndices[0]] + ", " + userInput[spaceIndices[0] + 1:spaceIndices[1]] + ", " + userInput[spaceIndices[1] + 1:spaceIndices[2]] + ", " + userInput[spaceIndices[2] + 1:] + ".")


newSentence3(str(input("Enter four words")))
