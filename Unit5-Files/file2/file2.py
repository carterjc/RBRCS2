# Carter
# file2.py


import random
import time


def clean(word):
    print(f"\n\n----{word}----\n\n")


# Part 1
# Create an object ‘story’ for the data inside story.txt

with open("story.txt", "r") as story:
    s_lines = story.readlines()

    # Write code to only display the first line of story
    clean("first_line")

    print(s_lines[0].strip("\n"))

    # Write code to only display the last line of story
    clean("last_line")

    print(s_lines[-1].strip("\n"))

    # Write code to only display even lines of story
    clean("even_lines")

    for i in range(1, len(s_lines), 2):
        print(s_lines[i].strip("\n"))

    # Write code to only display odd lines of story
    clean("odd_lines")

    for i in range(0, len(s_lines), 2):
        print(s_lines[i].strip("\n"))


# Part 2
# Create an object ‘name_list’ for the data inside names.txt

def sort_names(values):
    values = list(filter(lambda a: a.strip("\n") != "", values))
    values.sort(key=lambda x: x[0].lower())

    with open("names_sorted.txt", "w") as output:
        for name in values:
            print(name.strip("\n"))
            output.write(name.strip("\n") + "\n")


def add_name(name):
    with open("names.txt", "a+") as f:
        f.seek(0)
        lines = f.readlines()
        if lines[-1].endswith("\n"):
            f.write(name + "\n")
        else:
            f.write("\n" + name + "\n")
    sort_names(lines)


def delete_name(name):
    with open("names.txt", "r") as f:
        f.seek(0)
        lines = f.readlines()
        lines = [l.strip("\n") for l in lines]
    if name in lines:
        lines.remove(name)
    with open("names.txt", "w") as f:
        f.seek(0)
        for line in lines:
            f.write(line + "\n")
    sort_names(lines)


with open("names.txt", "r+") as name_list:

    # Write code or create a function to print all the names from
    # name_list

    clean("all_names")

    lines = name_list.readlines()
    for line in lines:
        if line != "\n":
            print(line.strip("\n"))

    # Write code to print only the names that start with ‘i’ from
    # name_list using startswith()

    clean("i_names")

    for line in lines:
        if line.startswith("I"):
            print(line.strip("\n"))

    # Write code to sort all the names from name_list, and store them
    # under a new file ‘names_sorted.txt’

    clean("names_sorted")

    name_list.seek(0)
    sort_names(name_list.readlines())

    # Manually add three more names to the end of ‘names.txt’

    add = True
    for line in lines:
        if line.strip("\n") == "Steve":
            add = False

    if lines[-1] == "\n" and add:
        name_list.write("Steve")
        name_list.write("\nSteven")
        name_list.write("\nSiry")
    elif add:
        name_list.write("\nSteve")
        name_list.write("\nSteven")
        name_list.write("\nSiry")

    # Sort, and update ‘names_sorted.txt’

    sort_names(name_list.readlines())

# Create a function add_name(name) that takes in a name as a
# parameter, and adds that name to ‘names.txt’, sorts the names, and
# updates ‘names_sorted.txt'

clean("add_name")

add_name("Carter")
add_name("Francis")

clean("del_name")

delete_name("Jessie")


# BONUS
# Create a Rock Paper Scissor game, or game of your choice
# Create a High Score list text file that sorts by high score
# Names that are present in the list shall not be duplicated
# If a high score is achieved by a current user on the list, replace
# that high score

def log_score(number):
    save = input("Do you want to save your score? (y/n)")
    if save.lower() == "y":
        name = str(input("What is your name?"))
        with open("scores", "a") as scores_f:
            scores_f.write(f"{name} - {str(number)}\n")
        with open("high_scores", "r") as h_scores:
            h_scores.seek(0)
            scores = []  # single line didn't work
            for l in h_scores.readlines():
                if l == "\n":
                    continue
                scores.append((l.split(" - ")[1], l.split(" - ")[2]))
            placed = False
            for i in range(len(scores)):
                if number > int(scores[i][1]):
                    scores.insert(i, (name, number))
                    print(f"Wow! You are now in position {i + 1} on the leaderboard!")
                    placed = True
                    break
            if len(scores) == 0:
                scores.append((name, number))
                print(f"Wow! You are now in position 1 on the leaderboard!")
            elif len(scores) <= 5 and not placed:
                scores.append((name, number))
                print(f"Wow! You are now in position {len(scores)} on the leaderboard!")
        with open("high_scores", "w") as h_scores:
            for i in range(len(scores)):
                if i > 5:
                    break
                num = str(scores[i][1]).strip("\n")
                h_scores.write(f"{i + 1} - {scores[i][0]} - {num}\n")
    else:
        print("Hope you had fun!")
    if input("Do you want to play again? (y/n)").lower() == "y":
        high_roller()
    else:
        print("Bye!")


def high_roller():
    print("""
Welcome to High Roller! In this exciting game, press start to roll a number. The higher the number,
the better! Good luck.
    """)
    input("Press enter to continue:")
    print("Rolling in\n3...")
    time.sleep(.1)
    print("2...")
    time.sleep(.1)
    print("1...")
    time.sleep(.1)
    print("Go")
    number = random.randint(0, 10000)
    print(f"Your number is {number}.")
    log_score(number)


high_roller()
