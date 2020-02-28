# Carter Costic
# guessNum.py

import random
max_range = 100


def play_game():
    number_choose = random.randint(0, max_range)
    guesses = 0
    right = False

    while not right:
        print("You have " + str(10 - guesses) + " guesses.")
        guess = int(input("Guess the number (1-" + str(max_range) + ")!"))
        guesses += 1
        diff = abs(guess - number_choose)

        if guess == number_choose:
            right = True
            play_again = str(input(("Congratulations, you got it right in " + str(guesses) +
                                    " tries!\nWant to play again? (Y/N)")))
            if play_again == "Y":
                play_game()
        elif diff <= int(max_range * .2):
            print("You're lukewarm")
            print("You're close...\nBy about " + str(diff + random.randint(0, diff)) + "!")
        elif diff <= int(max_range * .4):
            print("You're brisk")
        else:
            print("You're off base")

        if guesses >= 10:
            play_again = str(input("Game over. You had too many guesses. Do you want to play again?"))
            right = True


play_game()
print("Bye!")
