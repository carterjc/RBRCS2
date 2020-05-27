# Carter Costic
# Final Project - Part A


import random


# Defines a class for misc. shapes
class Shape:

    count = 0

    def __init__(self, s_type, size, color, border_width):
        self.s_type = s_type
        self.size = size
        color = self.color
        self.border_width = border_width
        Shape.count += 1
        self.shape_id = Shape.count

    def change_size(self, amount):
        if not isinstance(amount, int):
            print("Invalid amount!")
            return
        print(f"The size of {self.s_type.capitalize()} #{self.shape_id} changed from {self.size} to {self.size + amount}!")
        self.size += amount

    def change_b_wd(amount):
        if not isinstance(amount, int):
            print("Invalid amount!")
            return
        print(f"The border width of {self.s_type.capitalize()} #{self.shape_id} changed from "
              f"{self.border_width} to {self.border_width + amount}!")
        self.border_width += amount

    def roll(self):
        if self.s_type = "circle":
            print(f"{self.s_type.capitalize()} #{self.shape_id} rolled!")
        else:
            print(f"Sorry a {self.s_type.capitalize()} cannot roll!")


s_types = ["triangle", "circle", "square", "trapezoid"]
colors = {"red", "green", "blue", "yellow", "pink", "orange"}


shapes = []
for i in range(20):
    shapes.append(Shape(
        s_types[random.randint(0, len(s_types) - 1)],  # shape type
        random.randint(1, 20),  # shape size
        colors[random.randint(0, len(colors) - 1)],  # shape color
        random.randint(1, 5)))  # shape border width

# See if the 4th shape can roll
shapes[3].roll()

# Print the 7th shape's color
print(shapes[6].color.capitalize())

# Change the size of shape 15 by 3
shapes[14].change_size(3)

# Print the average size of the shapes
avg_size = 0
for shape in shapes:
    avg_size += shape.size
avg_size = avg_size/shapes

print(f"The average size of the shapes is {avg_size}!")
