# Carter Costic
# functions3.py


def maxNum(a, b, c):
    return max(c, max(a, b))


def sumAll(a, b, c, d, e):
    return a + b + c + d + e


def longestWord(a, b, c):
    return [str(i) for i in [a, b, c] if len(i) == (max(len(a), max(len(b), len(c))))]
    # return i for all a, b, c if the len(i) == the max length of a, b, c

###############


def cylVolume(radius, height):
    return (radius * 3.14) * height


def cubeVolume(base, height):
    return base * height


def sphereVolume(radius):
    return (4/3) * 3.14 * (radius**3)


def rectanglePrismVolume(width, height, length):
    return length * width * height

###############


def calculator():
    equation = str(input("Type 'list' to see a list of operations or press 's' to exit: "))
    if equation == "s":
        return
    try:
        print(eval(equation))
    except:
        print("Please try again.")
    calculator()
