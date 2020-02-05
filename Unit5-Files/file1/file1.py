# Carter
# file1.py

import requests
import random


def clean(word):
    print(f"\n\n----{word}----\n\n")


def get_quote():
    r = requests.get("https://programming-quotes-api.herokuapp.com/quotes/lang/en")
    index = random.randint(0, len(r.json()))
    quote = r.json()
    return quote[index]["en"] + "\n- " + quote[index]["author"]


# Part 1
# Create a variable ‘quote’ containing your favorite quote
quote = get_quote()

# Create a file object ‘write_file’ using open()

with open("file1", "w+") as write_file:
    write_file.write(quote)

# Create a file ‘file1.txt’ and set the mode to write
# Using .write(), update ‘file1.txt’ with the contents of ‘quote’
# Close the file object using .close()


# Part 2
# Create a function read_file(f) that will read and print any file
# passed as an argument using open()

def read_file(f):
    with open(f, "r") as file:
        print(file.read())


# Don’t forget to close the file object
# Read and Print ‘file1.txt’ using read_file(f)

clean("file1_read")

read_file("file1")


# Part 3
# Create a variable ‘quote2’ that contains another quote of your
# choice

quote2 = get_quote()

# Create a file object ‘append_file’ using the open() method, set the
# file as file1.txt, set the mode to append

with open("file1", "a") as append_file:
    append_file.write("\n\n" + quote2)

# Write the quote2 data to append_file
# Close the file object
# Read the updated file using read_file(f)

clean("new_file1_read")
read_file("file1")

# file1.txt should now have quote1 and quote2


# Part 4
# Create a function write2File(filename, stringObj) that takes in a
# filename, and a string object, and will overwrite a file with the
# content of the string object passed as an argument

def write2File(filename, stringObj):
    with open(filename, "w+") as file:
        file.write(stringObj)


# Create a variable ‘quote3’ that contains a third quote of your
# choice

quote3 = get_quote()

# Using write2File(fN, sO) create file file2.txt and supply quote3
# as an argument

write2File("file2", quote3)

# Use readFile(f) to read and print data

clean("file2_read")

read_file("file2")


# Part 5
# Create a function append2File(filename, stringObj) that takes in a
# filename, and a string object, that will append a file with the
# content of the string object passed as an argument

def append2File(filename, stringObj):
    with open(filename, "a") as file:
        file.write("\n\n" + stringObj)


# Create variable ‘quote4’ that contains a final quote of your choice

quote4 = get_quote()

# Using append2File(fN, sO) append quote4 to file2.txt

append2File("file2", quote4)

# Use readFile(f) to read and print data

clean("file2_new_read")

read_file("file2")

# BONUS
# Create a multiline string object

m_s_o = """0
1
2
3
4"""

with open("bonus", "w+") as f:
    f.write(m_s_o)

# Create a function to only read even lines of a string object passed
# as an argument


def bonus(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            print(lines[i])


clean("bonus")

bonus("bonus")
