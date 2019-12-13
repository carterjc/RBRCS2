# Carter
# benchmark1.py

import random


def print_line():
    print("\n\n----Section----\n\n")


print_line()

# Part 1: Variables & Expressions
# (1)
# Create a variable first_name and supply it with a string value
# Create a variable last_name and supply it with a string value
# Create a variable full_name which concatenates the previous two variables and a space

first_name = "Carter"  # Can't argue with the fundamentals
last_name = "Costic"  # Can't argue with the fundamentals
full_name = first_name + " " + last_name  # one way to do it, adds a space in between the vars
print(full_name)

print_line()

# (2)
# Create a variable num1 and supply it with an integer value
# Create a variable num2 and supply it with an integer value
# Create a variable num3 and supply it with the product of num1 and num2

num1 = 50  # Defining a variable, nothing to see here
num2 = 50  # Defining a variable, nothing to see here
num3 = num1 + num2  # Adding the two together
print(num3)

print_line()

# (3)
# Create a variable remainder and supply it with the remainder of any even integer divided by 2

remainder = 0  # Answer is always 0, no calculation necessary?
print(remainder)

print_line()

# (4)
# Create a variable random_int and supply it with a random integer from 0-10 (inclusive)
# using the Python randint() method

random_int = random.randint(0, 11)  # function is exclusive, so increase the range to 11 to include 10
print(random_int)

print_line()

# Part 2: Control Structures (Control Flow)
# (5)
# Create a series of control structures that will compare variables num4 and num5,
# (create and provide integer values of your choice)
# and provide print statements that display whether num4 or num5 is
# larger, or that they are equal.


# Defines the variables
num4 = 1
num5 = 2

if num4 > num5:  # if num4 is greater
    print("num4 is greater than num5")
if num4 < num5:  # if num5 is greater
    print("num5 is greater than num4")
else:  # if they are equal
    print("num4 is equal to num5")

print_line()

# (6)
# Create a series of control structures that will compare variables
# str1 and str2, (create and provide string values of your choice)
# and provide print statements that display whether str2 or str2 is
# longer in length, or that they are of equal length.

# Defines the variables
str1 = "pandabear"
str2 = "koalabear"

if len(str1) > len(str2):  # if the length of str1 is greater
    print("The length of str1 is greater than the length of str2")
if len(str1) < len(str2):  # if the length of str2 is greater
    print("The length of str2 is greater than the length of str1")
else:  # if the lengths are equal
    print("The length of str1 is equal to that of str2")

print_line()

# (7)
# Create a for loop that prints numbers 0 - 10 (including 10)

# one argument in the range function runs from 0 to that number exclusive, meaning it will stop at 10
for i in range(11):
    print(i)

print_line()

# (8)
# Create a for loop that prints all the even numbers from 0 - 10 (including 10)

# Same loop as before, but...
for i in range(11):
    if i % 2 == 0:  # this if checks if i divided by 2 leaves a remainder of 0 (if it's even)
        print(i)

print_line()

# (9)
# Create a for loop that prints the phrase “Computer Science” five times

for i in range(5):  # 0 - 4
    print("Computer Science")

print_line()

# (10)
# Create a while loop that takes a user input, and prints exactly what the user typed in.
# The loop shall terminate when the user enters the letter ‘Q’

stop = False  # if stop = True, the loop must 'stop'
while not stop:  # while stop is false
    user_input = input("Enter an input, or Q to quit:")
    if user_input == "Q":  # if the user inputs Q, stop
        stop = True
    else:
        print(user_input)

print_line()

# (11)
# Create a code block that prompts a user for a password (of your choice), and continuously prints “DENIED” if the
# password entered is incorrect. Once the password is entered properly, print “Congrats!”, ending the code block

password = "storedinplaintext"  # creates password variables
user_guess = ""  # creates variables for user input
while not user_guess == password:  # while the user guess is not the password
    user_guess = input("Enter the correct password:")
    if user_guess != password:  # if the user guess isn't the password
        print("DENIED")
print("Congrats!")  # if the loop ends, that means the password has been entered correctly

print_line()

# Part 3: Functions
# (12)
# Create a function say_hello() that prints the string “Hello!”
# Execute the function


def say_hello():  # defines the function
    print("Hello!")


say_hello()  # calls the function

print_line()

# (13)
# Create a function print_me() that takes in one parameter and prints that parameter.
# Execute the function


def print_me(to_print):  # creates a function with a parameter
    print(to_print)


print_me("dog")  # calls the function with the argument dog

print_line()

# (14)
# Create a function say_hello_to() that takes in one parameter and concatenates the parameter to the
# end of the phrase “Hello”, such that it will ‘Say Hello’ to the argument upon execution
# Execute the function


def say_hello_to(name):
    print(f"Hello, {name}.")  # formats the print statement to say Hello var name


say_hello_to("Doctor Manhattan")  # Calls the function with the argument Doctor Manhattan

print_line()

# (15)
# Create a function print_five() that prints the integer 5
# Execute the function


def print_five():  # https://youtu.be/wqzLoXjFT34
    print(5)


print_five()

print_line()

# (16) Create a function add_ten() that takes in one parameter and
# adds ten to it. This function shall print the result of said operation
# Execute the function


def add_ten(num):
    try:  # Tries to perform addition (checks if it is an int)
        print(num + 10)
    except:  # If it fails, insults the user
        print("Evil. You are evil. Don't toy with my function.")


add_ten("panda")
add_ten(10)

print_line()

# (17)
# Create a function max_num() that takes in two integer parameters and returns the largest of the two. If the integers
# are the same, it returns a string message stating that the integers are the same
# Create a variable store_max_num, and execute the function to set its value
# print(store_max_num)
# Execute the function


def max_num(num1, num2):
    if num1 == num2:  # if the two ints are equal
        return "The two integers are equal."
    else:
        return max(num1, num2)  # returns the max otherwise using the max function


store_max_num = max_num(1, 2)  # calls the function and stores the value
print(store_max_num)

print_line()

# (18)
# Create a function longest_string() that takes in two string parameters and returns the
# largest of the two. If the strings are the same, it returns a string message stating that they are the same
# Create a variable store_longest_string, and execute the function to set its value
# print(store_longest_string)
# Execute the function


def longest_string(str1, str2):
    if len(str1) > len(str2):  # if str1 is greater, return it
        return str1
    elif len(str1) < len(str2):  # if str2 is greater, return it
        return str2
    else:  # if they are equal, say so
        return "The length of the two strings are the same."


store_longest_string = longest_string("panda", "koala")
print(store_longest_string)

print_line()

# (19)
# Create a variable global_num, and provide it an integer value of  10
# Create a function increase_global_num() that will increase global_num by 1, and print its current value
# Execute the function

global_num = 10


def increase_global_num():
    global global_num  # grabs the global var
    global_num += 1
    print(global_num)


increase_global_num()

print_line()

# Part 4: Data Structures
# (20)
# Create a list string_list consisting of three strings of your choice
# Create a block of code that will add an item to the end of the list, supplied by user input
# print(string_list)

string_list = ["string1", "string2", "string3"]  # Creates the list
string_list.append(input("Enter a string:"))  # Adds a user defined string to the end
print(string_list)

print_line()

# (21)
# Create an empty list int_list
# Create a block of code that will add five random numbers to int_list using a control structure
# print(int_list)

int_list = []
for i in range(5):  # loops 5 times
    int_list.append(random.randint(0, 100))
print(int_list)

print_line()

# User for 22 & 23

bank_users = {
   0: {'name': 'Mr Watson', 'pin': '1234', 'balance': 500},
   1: {'name': 'Mr Melone', 'pin': '4567', 'balance': 600},
   2: {'name': 'Mrs Murphy', 'pin': '7890', 'balance': 700},
}

# (22)
# Create a function display_balance() that takes in a bank users name and pin number.
# This function shall display the current balance of the user passed as argument under the following conditions:
# The user exists in the bank_users dictionary
# The pin passed as a parameter is associated with the name passed as an argument


def display_balance(name, pin):  # creates a function with name and pin as the parameters
    for i, j in bank_users.items():  # loops through the user dictionary
        if j['name'] == name:  # if the name of a given index == name entered
            if pin == j['pin']:  # and pin is correct
                print(f"Hi, {name}! Your current balance is: ${j['balance']}\n")  # display balance
                return
    else:
        print(f"User '{name}' does not exist.")  # if user is not found, say it

# (23)
# Create a function withdraw() that takes in a bank users name, pin number and an amount to withdraw.
# This function shall reduce the users balance by the amount passed as an argument under the following conditions:
# The user exists in the bank_users dictionary
# The pin passed as a parameter is associated with the name passed as an argument
# The user has a balance that exceeds the amount passed as an argument to be withdrawn
# Execute display_balance() afterwards to the same user ensure the withdraw method works as expected


def withdraw(name, pin, amount):
    for i, j in bank_users.items():  # loops through the user dictionary
        if j['name'] == name:  # if the name of a given index == name entered
            if pin == j['pin']: # and pin is correct
                if amount <= j['balance']:  # and user has enough money
                    j['balance'] -= amount
                    print(f"Withdrawal accepted! (-${amount})\n")
                    display_balance(name, pin)
                else:
                    print("Insufficient funds.")  # Error handling
            else:
                print("Please enter the correct pin.")
            return
    else:
        print(f"User '{name}' does not exist.")  # if user is not found, say it


display_balance("Mr Watson", "1234")
withdraw("Mr Watson", "1234", 300)

print("\n----\n\nthe end.")
