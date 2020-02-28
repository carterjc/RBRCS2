# Carter Costic
# madlibs.py

import random
from stories import story4Real

storyPool = {  # creates a dictionary with the story and the number of nouns, verbs, and adjs
                "story1": [11, 4, 4, "story1"],
                "story2": [8, 0, 7, "story2"],
                "story3": [7, 4, 0, "story3"],
                "story4": [4, 10, 4, "story4"]
}


# Grabs the user's word, depending on the part of speech. It is stored in an array (not in this function)
def userInput(pos):
    return str(input("What is a " + str(pos) + "?"))


def chooseStory():  # Chooses a story at random and returns the number of nouns, verbs, adjs, and the title
    # index = "story" + str(random.randint(1, len(storyPool)))
    index = "story" + str(int(input("What story do you want to choose? There are no descriptions. (1, 2, 3, 4)")))
    return storyPool[index][0], storyPool[index][1], storyPool[index][2], storyPool[index][3]


def story1(nouns, verbs, adjs):  # The first story, takes the word arrays and places them correctly "Sports Team"
    story = "Nothing beats a game of " + nouns[0] + " on a " + adjs[0] + " " + nouns[1] + " day. Fans dress in their" \
            " team's " + nouns[2] + " and wave " + nouns[3] + " to show their support. Before the game, players will " \
            + verbs[0] + " with fans and autograph " + nouns[4] + " for them. It's a tradition to eat a " \
            + nouns[5] + " or " + nouns[6] + " at " + nouns[7] + " games. When a team scores a " + nouns[8] + "" \
            ", fans will " + verbs[1] + " and " + verbs[2] + ", and if you're " + adjs[1] + ", you can catch a flying" \
            + verbs[3] + ". Gift ships sell souvenirs, like" + adjs[2] + " " + nouns[9] + " and " + nouns[10] + "" \
            " to remember a " + adjs[3] + " day at the game."
    return story


def story2(nouns, verbs, adjs):  # Second story "Pizza Pizza"
    story = "Pizza was invented by a " + adjs[0] + " " + nouns[0] + " chef named " + nouns[1] + ". To make a pizza " \
            "you need to take a lump of " + nouns[2] + ", and make a thin, round " + adjs[1] + " " + nouns[3] + ". " \
            "Then you cover it with " + adjs[2] + " sauce, " + adjs[3] + " cheese, and fresh chopped " + nouns[4] + "" \
            ". Next you have to bake it in a very hot " + nouns[5] + ". When it is done, cut it into " + nouns[6] + "" \
            + " " + nouns[7] + ". Some kids like " + adjs[4] + " pizza the best, but my favorite is the " + adjs[5] + \
            "pizza. If I could, I would eat pizza " + adjs[6] + " times a day!"
    return story


def story3(nouns, verbs, adjs):  # Third story "The Longest Day of the Year"
    story = "Where I live, June " + nouns[0] + " is the longest day of the year. This means that the " + nouns[1] + "" \
            " " + verbs[0] + "for " + nouns[2] + " hours! It also means that kids have more time to " + verbs[1] + "" \
            " " + nouns[3] + " and go " + verbs[2] + " at the " + nouns[4] + ". Maybe the " + nouns[5] + " truck " \
            "will be in our neighborhood even later, too! This si the best day to " + verbs[3] + " my favorite summer" \
            " treat: " + nouns[6] + "."
    return story


def story4(nouns, verbs, adjs):  # Moby Dick story
    story = story4Real
    return story


def play():  # Main loop
    nouns = []
    verbs = []
    adjs = []
    nounsLength, verbsLength, adjsLength, index = chooseStory()  # defines number of words and the title
    for i in range(nounsLength):  # enters all of user's words
        nouns.append(userInput("noun"))
    for i in range(verbsLength):
        verbs.append(userInput("verb"))
    for i in range(adjsLength):
        adjs.append(userInput("adjective"))
    # Finds the correct story and calls it
    if index == "story1":
        story = story1(nouns, verbs, adjs)
    elif index == "story2":
        story = story2(nouns, verbs, adjs)
    elif index == "story3":
        story = story3(nouns, verbs, adjs)
    elif index == "story4":
        story = story4(nouns, verbs, adjs)
    else:
        story = "Error. Oops."
    print(story)  # prints the returned story
    # opens a text file (or creates one) with permissions to override the text
    with open("MadLibOutput.txt", "w+") as output:
        output.write(story)


play()
