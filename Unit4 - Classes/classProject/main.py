# Carter
# classProj.py

from classes import *
from c_bg import *

from os import system, name
import time


def clear():
    if name == 'nt':
        _ = system('cls')


# This function prints a title sequence for the game
def title():
    clear()
    print("Let's set the scene.\n\n\n")
    print("""
It's 2006. You're an up and coming banker at the world renowned Lehman Brothers Holdings, Inc bank.
Your goal is to climb to the top, but remember, don't get too greedy!
""")
    time.sleep(3)
    clear()
    print("\n--------\n\nBanker Simulator\n\n--------\n")
    input("Press enter to start your journey:")


# This function prints a series of exposition-y lines to introduce the game and its background
def expo():
    pass


def new_client(c_num):
    client = Client(clients[c_num])
    c_num -= -1
    pass


# This is the main game loop
def main():
    c_num = 0
    player = Banker()
    title()


main()
