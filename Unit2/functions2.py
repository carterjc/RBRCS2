# Carter Costic
# functions2.py

x = 1
y = 1
z = 1


def localx():
    x = 2
    print(x)


def localy():
    y = 3
    print(y)


def localz():
    z = 4
    print(z)


print(x, y, z)
localx()
localy()
localz()


def weirdx(a):
    global x
    x += a
    print(x)


def weirdy(b):
    global y
    y += b
    print(y)


def weirdz(c):
    global z
    z += c
    print(z)


print(x, y, z)
weirdx(31)
weirdy(13)
weirdz(131)

name, verb, place, food = "", "", "", ""


def updateName(n):
    global name
    name = n


def updateVerb(v):
    global verb
    verb = v


def updatePlace(p):
    global place
    place = p


def updateFood(f):
    global food
    food = f


def myStory():
    print(name + " " + verb + " " + place + " and eats " + food + ".")

updateName("Carter")
updateVerb("goes to")
updatePlace("house")
updateFood("pizza")

myStory()
