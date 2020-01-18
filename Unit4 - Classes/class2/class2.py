# Carter
# class2.py


import random


class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
        self.odo_miles = 0
        self.registered = False
        self.gas_in_tank = 15
        self.fuel_efficiency = 30
        self.max_fuel = 15

    def honk(self):
        print("Beep")

    def car_fax(self):
        if not self.registered:
            print_registered = "not "
        else:
            print_registered = ""
        print(f"Your car is {self.year} years old and is a {self.make} and {self.model}.")
        print(f"Also, your car has {self.odo_miles} miles and is {print_registered}registered.")

    def drive(self, miles_driven):
        car_miles = self.gas_in_tank * self.fuel_efficiency
        if self.registered:
            if miles_driven > 0:
                if car_miles >= miles_driven:
                    self.odo_miles += miles_driven
                    self.gas_in_tank -= round(miles_driven/self.fuel_efficiency, 1)
                else:
                    self.odo_miles += car_miles
                    self.gas_in_tank = 0
                    print("You ran out of gas!")
            else:
                print("Invalid miles driven")
        else:
            print("Your car is not registered. Get your act together.")

    def register(self):
        if not self.registered:
            self.registered = True
            print("Your car is now registered.")
        else:
            print("Your car is already registered.")

    def get_gas(self, money):
        gas_price = round(2.57 + random.uniform(-1, 1.5), 2)
        gas_needed = (self.max_fuel * self.fuel_efficiency) - (self.gas_in_tank * self.fuel_efficiency)
        if money > (gas_needed/self.fuel_efficiency) * gas_price:
            increase = round(gas_needed/self.fuel_efficiency, 2)
        else:
            increase = round(money/gas_price, 2)
        self.gas_in_tank += increase
        print(f"The price for gas is ${gas_price} per gallon. With ${money}, "
              f"your number of gallons increased by {increase}.")


car1 = Car(1, "cool", "95")
car2 = Car(15, "sweet", "J43")
car3 = Car(0, "uncool", "T87")
cars = [car1, car2, car3]

car1.honk()
car2.drive(2)
car3.car_fax()

for car in cars:
    car.register()

miles = 200
for car in cars:
    car.drive(miles)
    miles += 13

