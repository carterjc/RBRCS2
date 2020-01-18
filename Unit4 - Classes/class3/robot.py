# Carter
# robot.py

from class3 import Robot
import random

# print("Initializing two robots--")
# r1 = Robot('R2D2')
# r2 = Robot('C3PO')

# print("\nTesting Robot Methods--")
# r1.robot_info()
# r1.charge_robot()
# r2.robot_info()
# r2.charge_robot()
#
# print("\nLet the Battle Begin!--")
# r1.laser_attack(r2)
# r1.robot_info()
# r2.robot_info()
# r1.laser_attack(r2)
# r1.robot_info()
# r2.robot_info()
#
# while r2.health > 0:
#     r1.laser_attack(r2)


def print_line():
    print("\n----Section----\n")


# Bonus III
CPU = []
for i in range(5):
    name = "opponent" + str(i)
    CPU.append(Robot(name))

User = []
for i in range(5):
    name = "user" + str(i)
    User.append(Robot(name))

run = False
user_rnum = 0
cpu_rnum = 0


def attacks(robot, enemy, attack, user=False):
    if attack == 4:
        global run
        run = True
    elif attack == 1:
        robot.laser_attack(enemy)
    elif attack == 3:
        robot.charge_robot()
        print(f"{robot.robot_name} increased their battery by 25%.")
    else:
        robot.special_attack(enemy)
    if enemy.deactivated:
        if user:
            global cpu_rnum, opponent
            cpu_rnum += 1
            if cpu_rnum > 4:
                run = True
                print("Your opponent has run out of robots! You win!")
            else:
                opponent = CPU[cpu_rnum]
        else:
            global user_rnum
            user_rnum += 1


while not run:
    print_line()
    if user_rnum > 4:
        run = True
        print("You have run out of robots! You lose")
        break
    if cpu_rnum > 4:
        run = True
        print("Your opponent has run out of robots! You win!")
        break
    main_robot = User[user_rnum]
    opponent = CPU[cpu_rnum]
    print(f"Your battery is at {main_robot.battery}% and your health is at {main_robot.health}.\n")
    print("Attack options:\n1: Basic attack\n2: Special attack\n3: Charge\n4: Run")
    action = int(input("Enter your attack choice:"))
    print("\n\n")
    if action == 4:
        run = True
        print("You fled like a baby robot. Disgraceful.")
        break
    print("----User attack----\n")
    attacks(main_robot, opponent, action, True)
    if not run:
        print("\n----Opponent attack----\n")
        robot_attack = random.randint(1, 2)
        if opponent.battery <= 25:
            robot_attack += 1
        attacks(opponent, main_robot, robot_attack)




