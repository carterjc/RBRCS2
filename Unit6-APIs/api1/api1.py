# Carter Costic
# api1.py

import requests, json


def clean(word):
    print(f"\n\n----{word}----\n\n")


# Part 1
# At the top of your file import requests, and json

# Using the example from the API Slides [link] create a request to
# http://api.open-notify.org/astros.json

response = requests.get("http://api.open-notify.org/astros.json")
response = response.json()

clean("First API Response")
print(response)

# Print the response

# Create a loop that will iterate over the response object only
# printing its keys

clean("JSON Keys")
for key in response.keys():
    print(key)

# Create a loop that will iterate over the “people” array of the
# response object and only print the “name” values

clean("Names")
for person in response["people"]:
    print(person["name"])

# Part 2
# Using this joke API create a program that will make a random joke
# generator

# This program shall take user input to ask a user if they would like
# to hear a joke

# Step 1: Read at the API documentation
# Step 2: Find the endpoint that will return one random joke, and test
# in a browser window
# Step 3: Create an API call that will return a random joke
# Step 4: Test your code to see if you get the proper results
# Step 5: Extract the ‘setup’ and the ‘punchline’ from each joke
# Step 6:
# Create a loop that will prompt the user to hear a joke
# If the user replies YES (or a positive response of your choice)
# display the setup, and after the user hits ENTER display the punchline
# If the user replies NO (or a negative response of your choice)
# exit the program
# All other inputs should print an error for invalid input


# BONUS
# Create a joke class that will return a new joke using a method
# Allow the user three attempts to guess the punchline before it is
# revealed

clean("Joke Program")


class Joke:
    joke_tally = 0

    def __init__(self):
        self.begin = ""
        self.punchline = ""
        self.guessed = False

    def get_joke(self):
        request = requests.get("https://official-joke-api.appspot.com/random_joke")
        request = request.json()
        self.begin = request["setup"]
        self.punchline = request["punchline"]
        Joke.joke_tally -= -1

    def ask_joke(self, difficulty=.4):
        print("Hi! Try to guess my joke!\n\n----")
        print(self.begin)
        print("----\n\nYou have 3 tries!\n")
        for i in range(1, 4):
            usr_guess = input(f"Alright, this is try #{i}. What do you think the punchline is?\n")
            char_match = 0
            for segment in usr_guess.split(" "):
                if segment.lower() in self.punchline.lower():
                    char_match += len(segment)
            if char_match/len(self.punchline) >= difficulty:
                print("You got it! Wow!\n")
                print(self.punchline)
                self.guessed = True
                break
            else:
                print("Close... try again!\n")
        if not self.guessed:
            print("Your tries are up... better luck next time!\n")
            print(self.punchline)


while True:
    cont = input("Would you like to hear a joke? (y/n)")
    if cont == "n":
        break
    elif cont == "y":
        joke = Joke()
        joke.get_joke()
        joke.ask_joke()
    else:
        print("Please enter a response in a valid format.")
        continue
