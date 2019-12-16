# Carter
# class3.py


class Robot:
    robot_population = 0
    robot_list = []

    def __init__(self, name):
        self.robot_name = name
        self.battery = 100
        self.health = 200
        self.deactivated = False
        self.robot_num = self.robot_population
        Robot.robot_population += 1
        Robot.robot_list.append(self)
        print(f"Robot {self.robot_name} #{self.robot_num} ready for instruction.")

    def robot_info(self):
        deactivated_statement = "not " if self.deactivated else ""
        print(f"I am {self.robot_name} #{self.robot_num}. \n"
              f"I am at {self.battery}% battery, have {self.health} health, and am {deactivated_statement}activated.")

    def charge_robot(self):
        if self.deactivated:
            return
        if self.battery > 75:
            self.battery = 100
        else:
            self.battery += 25

    def laser_attack(self, robot):
        if self.battery < 10 or self.deactivated:
            return
        self.battery -= 10
        robot.health -= 20
        if robot.health < 1:
            robot.battery = 0
            robot.deactivated = True
            robot.health = 0
        print(f"{self.robot_name} attacked {robot.robot_name} for 20 damage.\n"
              f"{robot.robot_name} has {robot.health} health.")
        if self.battery <= 0:
            self.deactivated = True

    def special_attack(self, robot):
        if self.battery < 25 or self.deactivated:
            return
        self.battery -= 25
        robot.health -= 50
        if robot.health < 1:
            robot.battery = 0
            robot.deactivated = True
            robot.health = 0
        print(f"{self.robot_name} attacked {robot.robot_name} specially for 50 damage.\n"
              f"{robot.robot_name} has {robot.health} health.")
        if self.battery <= 0:
            self.deactivated = True

        @classmethod
        def display_all_robots():
            print("\n--Inventory check--\n")
            for robot in Robot.robot_list:
                print(f"{robot.robot_name} #{robot.robot_num} reporting")
