# Carter
# 2/Dec/19
# class1.py


class Student:

    def __init__(self, first_name, last_name, age, fav_subject):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.fav_subject = fav_subject

    def greeting(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}. "
              f"I am {self.age} and my favorite subject is {self.fav_subject}.")

    def birthday(self):
        self.age += 1
        print(f"Happy birthday, {self.first_name}!")
        for i in range(1, self.age):
            print("Are you " + str(i) + "?")
        print("Yay!")

    def get_fav_subject(self):
        return self.fav_subject


def print_line():
    print("\n\n----Section----\n\n")


# Instantiate 5 Student objects, at least two shall have an age of 15

student1 = Student("Carter", "Costic", 15, "Computer Science")
student2 = Student("Herlinda", "Troutman", 16, "Cooking")
student3 = Student("Margaret", "Spaulding", 14, "Basket Weaving")
student4 = Student("Jeanette", "Horowitz", 15, "Networking")
student5 = Student("Thomas", "Hackney", 16, "Lunch")

# Print the first name of two objects

print(student1.first_name)
print(student2.first_name)
print_line()

# Print the age of two different objects

print(student3.age)
print(student4.age)
print_line()

# Print the last name of two different objects

print(student5.last_name)
print(student1.last_name)
print_line()

# Create a list student_list with all of your Student objects

student_list = [student1, student2, student3, student4, student5]

# Loop over this list and call the greeting() method during each
# iteration

for student in student_list:
    student.greeting()
print_line()

# Create another loop, and only print the names and ages of students
# that have an age greater than 15

for student in student_list:
    if student.age > 15:
        print(f"{student.first_name} {student.last_name} is {student.age}.")
print_line()

# Call the birthday method on students who do not have an age older
# than 15, until they are at least 16, and repeat the previous loop

for student in student_list:
    while student.age <= 15:
        student.birthday()
