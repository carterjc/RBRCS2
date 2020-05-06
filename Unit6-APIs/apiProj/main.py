# Carter Costic
# apiProj

from crud_actions import *


# dev url
base_url = "http://localhost:8080/api/v1/"
access = -1


# Basic line break function
def line_br(word):
    print(f"\n\n----{word}----\n\n")


# Main loop once logged in
def landing():
    line_br("Main")
    print("""0 - Sign out
1-5: Employee functions
6-10: Customer functions
11-15: Sale functions
16-20: Department functions
21-25: Location functions
26-30: Position functions

1st - List all
2nd - Choose one
3rd - Edit item
4th - Create item
5th - Delete item""")
    line_br("Input")
    # Add error handling
    choice = ""
    while not choice.isdigit():
        choice = input("Select a function:")
    choice = int(choice)
    line_br("Response")
    if choice == 0:
        sign_out()
    elif choice == 1:
        get_all("employees", "employees", "emp_id", "emp_fn", "emp_ln")
    elif choice == 2:
        get_one("employees", "employee", "emp_id", "emp_fn", "emp_ln")
    elif choice == 3 and access >= 1:
        edit_item("employees", "employee", "emp_id", "emp_fn", "emp_ln", "emp_id")
    elif choice == 4 and access >= 1:
        add_item("employees", "employee", "emp_id", "emp_fn", "emp_ln")
    elif choice == 5 and access >= 2:
        del_item("employees", "employee", "emp_id", "emp_fn", "emp_ln")
    elif choice == 6:
        get_all("customers", "customers", "customer_id", "customer_fn", "customer_ln")
    elif choice == 7:
        get_one("customers", "customer", "customer_id", "customer_fn", "customer_ln")
    elif choice == 8 and access >= 1:
        edit_item("customers", "customer", "customer_id", "customer_fn", "customer_ln", "customer_id")
    elif choice == 9 and access >= 1:
        add_item("customers", "customer", "customer_id", "customer_fn", "customer_ln")
    elif choice == 10 and access >= 2:
        del_item("customers", "customer", "customer_id", "customer_fn", "customer_ln")
    elif choice == 11:
        get_all("sales", "sales", "sale_id", "amount", "installments")
    elif choice == 12:
        get_one("sales", "sale", "sale_id", "amount", "installments")
    elif choice == 13 and access >= 1:
        edit_item("sales", "sale", "sale_id", "amount", "installments", "sale_id")
    elif choice == 14 and access >= 1:
        add_item("sales", "sale", "sale_id", "amount", "installments")
    elif choice == 15 and access >= 2:
        del_item("sales", "sale", "sale_id", "amount", "installments")
    elif choice == 16:
        get_all("departments", "departments", "dep_id", "dep_name", "dep_description")
    elif choice == 17:
        get_one("departments", "department", "dep_id", "dep_name", "dep_description")
    elif choice == 18 and access >= 1:
        edit_item("departments", "department", "dep_id", "dep_name", "dep_description", "dep_id")
    elif choice == 19 and access >= 1:
        add_item("departments", "department", "dep_id", "dep_name", "dep_description")
    elif choice == 20 and access >= 2:
        del_item("departments", "department", "dep_id", "dep_name", "dep_description")
    elif choice == 21:
        get_all("locations", "locations", "location_id", "loc_name", "address")
    elif choice == 22:
        get_one("locations", "location", "location_id", "loc_name", "address")
    elif choice == 23 and access >= 1:
        edit_item("locations", "location", "location_id", "loc_name", "address", "location_id")
    elif choice == 24 and access >= 1:
        add_item("locations", "location", "location_id", "loc_name", "address")
    elif choice == 25 and access >= 2:
        del_item("locations", "location", "location_id", "loc_name", "address")
    elif choice == 26:
        get_all("positions", "positions", "position_id", "pos_title", "pos_description")
    elif choice == 27:
        get_one("positions", "position", "position_id", "pos_title", "pos_description")
    elif choice == 28 and access >= 1:
        edit_item("positions", "position", "position_id", "pos_title", "pos_description", "position_id")
    elif choice == 29 and access >= 1:
        add_item("positions", "position", "position_id", "pos_title", "pos_description")
    elif choice == 30 and access >= 2:
        del_item("positions", "position", "position_id", "pos_title", "pos_description")
    else:
        print("Invalid input or insufficient permissions: Try again.")


# Welcome function
def welcome(user):
    # Allow MOTD alteration with .txt file or database addition?
    print(f"""
Welcome, {user["emp_fn"]} {user["emp_ln"]}!""")
    global access
    access = user['privilege']
    if access == 2:
        print("You have full access to the employee database")
    elif access == 1:
        print("You do not have deletion privileges")
    else:
        print("You have view only access")


# Sign out function
def sign_out():
    print("Successfully signed out!")
    global access
    access = -1


# Sign in function
def sign_in():
    email = input("Please enter your email address:")
    password = input("Please enter your password:")

    line_br("Response")

    add_url = "employees"
    res = requests.get(base_url + add_url).json()

    logged_in = False
    login_user = {}

    # Verification
    # Welcome message or invalid em/pw

    for user in res:
        if email.lower() == user['email'].lower():
            if user['password'].lower() == password.lower():
                print("Success!")
                login_user = user
                logged_in = True
            else:
                print("Invalid password. Try again.")
    if not logged_in:
        print("Invalid email address. Try again.")
        line_br("Sign in")
    else:
        welcome(login_user)


# Main loop
def main():
    print("""
Welcome to the Employee Management System created by the developers at Costic Software Solutions!
Please sign in below:""")
    line_br("Sign in")
    global access
    while access == -1:
        sign_in()
    while access >= 0:
        landing()


main()
