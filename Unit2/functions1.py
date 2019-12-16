# Carter Costic
# functions1.py

from datetime import date
import datetime
import math


def myName():
    print("Carter Costic")


myName()


def myFav():
    print("Blue")


myFav()


def myHobby():
    print("CyPat")


myHobby()


def todaysDate(d, m, y):
    print("Today is " + str(d) + "/" + str(m) + "/" + str(y))


todaysDate(17, 9, 2019)


def f2c(fTemp):
    return (fTemp-32) * 5/9


print(f2c(80))


def ageCalc(d, m, y):
    todayDay = date.today().strftime("%d")
    todayMonth = date.today().strftime("%m")
    year = date.today().strftime("%y")
    dayDiff = abs(int(todayDay) - d)
    monthDiff = abs(int(todayMonth) - m)
    yearDiff = abs(int(year) - y)
    return "You are " + str(dayDiff) + " days, " + str(monthDiff) + " months, and " + str(yearDiff) + " years old!"


print(ageCalc(5, 3, 4))


def factorial(num):
    result = 1
    for i in range(1, num+1):
        result = result * i
    return result


print(factorial(7))


def betterFactorial(num):
    print(math.factorial(num))


def experimental(num):
    return [1 * i for i in range(1, num+1)]


experimental(7)