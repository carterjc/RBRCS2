# Carter
# classProj.py

from classes import *
from c_bg import *

from os import system, name
import time
import random


c_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
g_time = 1  # starts in 2006 Q1, represents quarters since
end = False


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
def expo(player):
    curr_year = int(2006 + ((g_time - 1) / 4))
    quarter = g_time % 4 if g_time % 4 > 0 else 4
    print(f"""
It's {curr_year} Q{quarter}. You have ${int(player.money):,d} after {round((g_time - 1) / 4)} year{"s" if round((g_time - 1) / 4) != 1 else ""} at Lehman.
With the new quarter comes a new client.\n
----""")


def g_exit(player):  # exit the company gracefully
    print(f"""
After long last, you decide to leave Lehman Brothers behind and its competitive, exploitative nature.
It's for the best. With your nest egg of ${int(player.money):,d}, you should be able to start anew.

----

In {(10 - g_time) / 4} years, you turn on the news, only to see the collapse of your company. You got out before it all
came crashing down.""")
    input("Press enter to complete the game:")
    global end
    end = True


def f_exit(client, player):  # exit the company forcefully after you get fired
    print(f"""
    You turn away {client.name} much to the dismay of management.

    One day, you are called down to HR. With imaginary clouds darkening around your head, you don't feel particularly 
    confident.

    "We need to let you go. You have three strikes. That's enough."

    You knew it was coming, but it still hits hard. With ${int(player.money):,d}, you exit the company to start fresh
    somewhere else.

    ----""")
    input("Press enter to complete the game:")
    global end
    end = True


def financial_crisis(player):  # financial crisis time (crab rave)
    print("""
2008 Q3. It happens. No one knows how it wasn't obvious, but the feelings are certainly felt now.
Major banks crumble as the housing market collapses. Lehman Brothers goes under and you are out of a job.
Your savings are wiped (those vested shares aren't looking so great now). Hopefully one day you'll get back on your
feet.
    """)
    input("Press enter to complete the game:")


# Defines a new client and begins interaction
def new_client(player):
    global c_num
    selection = c_num[random.randint(0, len(c_num) - 1)]
    client = Client(clients[selection])
    c_num.remove(selection)
    print(f"""
Your new client is ready. {client.name} from a family of {len(client.family)}.
    """)
    input(f"Press enter to beckon in {client.name}:")
    clear()
    if random.randint(0, 1) == 0:  # client asks for loan
        client.give_info(True)
        decide(client, player)
    else:
        client.give_info(False)
        decide(client, player)


def decide(client, player):  # Player chooses to grant loan/investment or not
    decision = input("\nWhat do you decide? Will you sign the client? (y/n)")
    clear()
    if decision.lower() == "n":
        player.strikes -= -1
        if player.strikes >= 3:
            f_exit(client, player)
            return
        print(f"""
Though it is tough, you make the decision to turn away the client. With confusion, {client.name} turns away and leaves.

Later in the day, your manager walks in.
"What's that I here about you ditching a client? We don't get do that here! You're walking on thin ice."

So that's a strike. Let's see what happens next quarter.

----
""")
    elif decision.lower() == "y":
        print(f"""
You know this has the possibility to ruin this person and their family if things go south, but you sign the deal anyway.
The pressure management puts on you is too much; you can't just turn down money.
In a few weeks, your check comes in: ${int((client.asset_v + client.income)/5):,d}.
Soon, the quarter comes to a close.

----
        """)
        player.money += (client.asset_v + client.income)/5
    else:
        print("Not a valid input. Please try again.")
        decide(client, player)
    global g_time
    g_time -= -1


def quarterly_survey(player):  # Gauges player sentiment and allows for the player to leave the bank
    print(f"""
The quarter is over. As the earnings frenzy ends, a satisfaction report gets placed on your desk.
Answer truthfully.
""")
    input("Press enter to take the survey:")
    clear()
    q1 = input("Are you happy at your job right now? (y/n)\n")
    clear()
    if q1 == "y":
        q2 = input("Do you like the benefits Lehman Brothers offers their employees? (y/n)\n")
        clear()
        if q2 == "y":
            print("""
We appreciate your honesty. We look forward to your feedback in the future.
            """)
        elif q2 == "n":
            print("""
We are sorry to hear that. Lehman Brothers will make efforts to improve these areas in the future.
            """)
        else:
            print("Invalid input. Please try again.")
            quarterly_survey(player)
    elif q1 == "n":
        q2_1 = input("Do you plan on exiting your position? (y/n)\n")
        clear()
        if q2_1 == "y":
            exit = input("Press (y) to exit your position and retire.\n")
            clear()
            if exit == "y":
                g_exit(player)
        elif q2_1 == "n":
            print("""
We are sorry to hear that. Lehman Brothers will make efforts to improve these areas in the future.
            """)
        else:
            print("Invalid input. Please try again.")
            quarterly_survey(player)
    else:
        print("Invalid input. Please try again.")
        quarterly_survey(player)


# This is the main game loop
def main():
    player = Banker()
    title()
    clear()
    while g_time <= 10:
        expo(player)
        new_client(player)
        if end:
            break
        quarterly_survey(player)
        if end:
            break
        input("Press enter to continue into the next quarter:")
        clear()
    if g_time >= 10:
        financial_crisis(player)
    clear()
    print("""
Thanks for playing Banker Simulator. Hope you didn't partake in the global financial meltdown!
    """)
    time.sleep(2)


main()
