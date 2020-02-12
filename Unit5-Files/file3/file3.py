# Carter
# file3.py

# Part 1
# Using capitals.csv create a program that prompts a user for a
# Country name or Capital name
# If the user enters a Capital name, print its corresponding Country
# If the user enters a Country name, print its corresponding Capital
# This program shall loop until a user enters a statement to quit

country_map = {'A': 2, 'B': 19, 'C': 39, 'D': 60, 'E': 65, 'F': 74, 'G': 82, 'H': 97, 'I': 100, 'J': 109, 'K': 113, 'L': 119, 'M': 128, 'N': 162, 'U': 232, 'O': 164, 'P': 165, 'Q': 177, 'R': 178, 'S': 183, 'T': 219, 'V': 240, 'W': 244, 'Y': 247, 'Z': 248}
capital_map = {'S': [2, 11, 29, 31, 36, 46, 53, 64, 69, 74, 77, 90, 93, 111, 128, 147, 162, 176, 188, 191, 198, 207, 211, 215, 218, 247], 'K': [3, 60, 109, 117, 131, 150, 158, 182, 189, 212, 232, 233], 'E': [4, 193, 226, 246], 'T': [5, 10, 28, 72, 75, 84, 98, 103, 110, 115, 124, 178, 208, 224, 227, 239], 'A': [6, 8, 52, 71, 73, 86, 88, 112, 113, 129, 151, 156, 157, 170, 173, 190, 228, 229, 234], 'P': [7, 26, 39, 42, 58, 76, 79, 81, 97, 116, 137, 142, 143, 159, 168, 169, 199, 205, 213, 225, 240], 'L': [9, 30, 82, 127, 130, 171, 175, 201, 222, 235, 248], 'B': [12, 18, 22, 24, 25, 33, 35, 38, 44, 47, 50, 83, 85, 95, 99, 104, 118, 121, 133, 161, 179, 180, 185, 195, 200, 216, 221], 'Y': [13, 40, 59, 149], 'O': [14, 37, 41, 163], 'G': [15, 32, 43, 87, 92, 96, 183, 206], 'C': [16, 61, 68, 80, 94, 139, 186, 230, 237, 242, 244], 'V': [17, 119, 125, 126, 134, 196, 241], 'N': [19, 45, 57, 89, 101, 114, 136, 146, 152, 155, 160, 166, 223], 'M': [20, 23, 51, 70, 122, 123, 132, 135, 138, 140, 145, 154, 164, 172, 181, 187, 203, 210, 214, 238, 245], 'D': [21, 62, 65, 105, 106, 177, 194, 217, 219, 220], 'H': [27, 55, 66, 78, 91, 202, 204, 243, 249], 'R': [34, 63, 100, 108, 120, 144, 192], 'F': [48, 197, 231], 'W': [49, 56, 148, 153, 174, 236], 'Z': [54], 'Q': [67], 'J': [102, 107, 167, 184, 209], 'U': [141], 'I': [165]}


def gather_data():
    capitals = open("capitals.csv", "r")
    global cap_count_dat
    cap_count_dat = capitals.readlines()
    # Either store in RAM? (locally) or read file for specific lines each time
    # Undecided on efficiency
    capitals.close()


def user_prompt():
    enter = input("Please enter a capital or country:")
    if isinstance(enter, int):
        print("Invalid input. Please enter a capital or country.")
        return
    elif True in [char.isdigit() for char in enter]:
        print("Invalid input. Please enter a capital or country.")
        return
    for index in range(country_map[enter[0].upper()] - 1, len(cap_count_dat)):
        country = cap_count_dat[index].split(",")[0].lower()
        if enter.lower() in country:
            str_len = len(cap_count_dat[index].split(','))
            if str_len > 3:
                capital = cap_count_dat[index].split(',')[1:str_len - 1]
            else:
                capital = cap_count_dat[index].split(',')[1]
            capital_f = "".join([elem for elem in capital])
            # String version of capital
            print(f"The capital of {country.title()} is {capital_f}.")
            break
    for index in capital_map[enter[0].upper()]:
        str_len = len(cap_count_dat[index - 1].split(','))
        if str_len > 3:
            capital = cap_count_dat[index - 1].split(',')[1:str_len - 1]
        else:
            capital = cap_count_dat[index - 1].split(',')[1]
        capital_f = "".join([elem for elem in capital])
        if enter.lower() in capital_f.lower():
            print(f"The country with the capital {capital_f} is {cap_count_dat[index - 1].split(',')[0]}.")
            break


def main():
    gather_data()
    cont = "y"
    while cont.lower() == "y":
        user_prompt()
        cont = input("Do you want to find another capital/country? (y/n)")
    print("Bye!")


main()
