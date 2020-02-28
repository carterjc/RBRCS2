# Carter Costic
# madlibs.py

import random
from stories import story4Real

storyPool = {  # creates a dictionary with the story and the
                "story1": [
                    ["sport", "adjective", "season", "article of clothing", "noun", "verb", "noun", "food",
                     "snack food", "sport", "noun", "verb", "verb", "adverb", "adjective", "verb", "adjective",
                     "noun", "noun", "adjective"],
                    20,
                    "story1"
                ],
                "story2": [
                    ["adjective", "nationality", "person", "noun", "adjective", "noun", "adjective", "adjective",
                     "plural noun", "noun", "number", "shapes", "food", "food", "number"],
                    15,
                    "story2"
                ],
                "story3": [
                    ["number", "noun", "verb", "number", "verb", "place", "verb ending in -ing", "place", "food",
                     "verb", "food"],
                    11,
                    "story3"
                ],
                "story4": [
                    ["noun", "adjective", "place", "season", "type of dog", "person", "place", "day"],
                    8,
                    "story4"
                ]
}


# Grabs the user's word, depending on the part of speech. It is stored in an array (not in this function)
# Uses the total amount of words and the current word to inform the user of his/her progress
def userInput(pos, num, current):
    return str(input("What is a " + str(pos) + "? - " + str(current) + "/" + str(num)))


def chooseStory():  # Chooses a story at random and returns the number of nouns, verbs, adjs, and the title
    # index = "story" + str(random.randint(1, len(storyPool)))
    index = "story" + str(input("What story do you want to choose?\n"
                                    "1 is about sports.\n"
                                    "2 is about pizza.\n"
                                    "3 is about a year.\n"
                                    "4 is a secret.\n(1, 2, 3, 4, quit)"))
    return index


def story1(words):  # The first story, takes the word arrays and places them correctly "Sports Team"
    story = "Nothing beats a game of " + words[0] + " on a " + words[1] + " " + words[2] + " day. Fans dress in their" \
            " team's " + words[3] + " and wave " + words[4] + " to show their support. Before the game, players will " \
            + words[5] + " with fans and autograph " + words[6] + " for them. It's a tradition to eat a " \
            + words[7] + " or " + words[8] + " at " + words[9] + " games. When a team scores a " + words[10] + "" \
            ", fans will " + words[11] + " and " + words[12] + " " + words[13] + ", and if you're " + words[14] + ", you can catch a flying " \
            + words[15] + ". Gift ships sell souvenirs, like " + words[16] + " " + words[17] + " and " + words[18] + "" \
            " to remember a " + words[19] + " day at the game."
    return story


def story2(words):  # Second story "Pizza Pizza"
    story = "Pizza was invented by a " + words[0] + " " + words[1] + " chef named " + words[2] + ". To make a pizza " \
            "you need to take a lump of " + words[3] + ", and make a thin, round " + words[4] + " " + words[5] + ". " \
            "Then you cover it with " + words[6] + " sauce, " + words[7] + " cheese, and fresh chopped " + words[8] + "" \
            ". Next you have to bake it in a very hot " + words[9] + ". When it is done, cut it into " + words[10] + "" \
            + " " + words[11] + ". Some kids like " + words[12] + " pizza the best, but my favorite is the " + words[13] + \
            " pizza. If I could, I would eat pizza " + words[14] + " times a day!"
    return story


def story3(words):  # Third story "The Longest Day of the Year"
    story = "Where I live, June " + words[0] + " is the longest day of the year. This means that the " + words[1] + "" \
            " " + words[2] + "for " + words[3] + " hours! It also means that kids have more time to " + words[4] + "" \
            " " + words[5] + " and go " + words[6] + " at the " + words[7] + ". Maybe the " + words[8] + " truck " \
            "will be in our neighborhood even later, too! This si the best day to " + words[9] + " my favorite summer" \
            " treat: " + words[10] + "."
    return story


def story4():  # Moby Dick story
    story = story4Real
    return story


def play():  # Main loop
    index = chooseStory()
    while index == "story1" or index == "story2" or index == "story3" or index == "story4":
        words = []
        # defines number of words and the title
        descriptiveWord, numOfWords, index = storyPool[index][0], storyPool[index][1], storyPool[index][2]
        for i in range(numOfWords):  # enters all of user's words
            words.append(userInput(descriptiveWord[i], numOfWords, i + 1))
        # Finds the correct story and calls it
        if index == "story1":
            story = story1(words)
        elif index == "story2":
            story = story2(words)
        elif index == "story3":
            story = story3(words)
        elif index == "story4":
            story = story4()
        else:
            story = "Error. Oops."
        print(story)  # prints the returned story
        # opens a text file (or creates one) with permissions to override the text
        with open("MadLibOutput.txt", "w+") as output:
            output.write(story)
        index = chooseStory()
    print("Cool cool cool cool")
    return


play()  # actually calls the main function
