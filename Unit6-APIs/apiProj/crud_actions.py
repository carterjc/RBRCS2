import requests


# dev url
base_url = "http://localhost:8080/api/v1/"


# Gives a brief summary of all items
def get_all(url, desc, f_term, s_term, t_term):
    res = requests.get(base_url + url).json()
    print(f"Here is a quick output of the current {desc}:\n")
    for item in res:
        print(f"{item[f_term]} - {item[s_term]}, {item[t_term]}\n")


# Gives an in-depth summary of one item
def get_one(url, desc, f_term, s_term, t_term):
    # Output item IDs
    res = requests.get(base_url + url).json()
    for item in res:
        print(f"{item[f_term]} - {item[s_term]}, {item[t_term]}\n")
    # Error handling
    item_id = ""
    while not item_id.isdigit() or item_id not in [str(item[f_term]) for item in res]:
        item_id = input(f"What is the ID of the {desc}?")
    url += "/" + str(item_id)
    res = requests.get(base_url + url).json()[0]
    print(f"Here is a detailed output of the selected {desc}:\n--\n")
    for key, value in res.items():
        print(f"{key}: {value}")


# Modify an item's properties
def edit_item(url, desc, f_term, s_term, t_term, exc):
    # Output item IDs
    res = requests.get(base_url + url).json()
    for item in res:
        print(f"{item[f_term]} - {item[s_term]}, {item[t_term]}\n")
    # Error handling
    item_id = ""
    while not item_id.isdigit() or item_id not in [str(item[f_term]) for item in res]:
        item_id = input(f"What is the ID of the {desc} you want to edit?")
    url += "/update/" + str(item_id)
    new_edit_item = {}
    for item in res:
        if item[f_term] == int(item_id):
            new_edit_item = item
    for key in new_edit_item.keys():
        if key == exc:
            continue
        if str(input(f"If you want to enter a new {key} type 'y':")).lower() == "y":
            new_edit_item[key] = str(input(f"Enter a new {key}:"))
    res = requests.post(base_url + url, data=new_edit_item).json()
    if len(res) == 1:
        print(f"There was an error while editing {desc} {item_id}")
    else:
        print(f"{desc.capitalize()} with ID of {item_id} edited successfully")


# Adds an item
def add_item(url, desc, f_term, s_term, t_term):
    # Output item IDs
    res = requests.get(base_url + url).json()
    print(f"Existing {desc}:\n")
    for item in res:
        print(f"{item[f_term]} - {item[s_term]}, {item[t_term]}")
    print("\n")
    # Error handling
    new_item = res[0]
    for key in new_item.keys():
        if key == f_term:
            continue
        new_item[key] = str(input(f"Enter a {key}:"))
    res = requests.post(base_url + url, data=new_item).json()
    if len(res) == 1:
        print(f"There was an error while creating {desc}")
    else:
        print(f"{desc.capitalize()} created successfully")


# Deletes an item
def del_item(url, desc, f_term, s_term, t_term):
    # Output item IDs
    res = requests.get(base_url + url).json()
    for item in res:
        print(f"{item[f_term]} - {item[s_term]}, {item[t_term]}\n")
    # Error handling
    item_id = ""
    while not item_id.isdigit() or item_id not in [str(item[f_term]) for item in res]:
        item_id = input(f"What is the ID of the {desc} to delete?")
    url += "/" + str(item_id)
    res = requests.delete(base_url + url).json()
    fail = False
    if "error" in [key for value, key in res.items()]:
        fail = True
    if not fail:
        print(f"{desc.capitalize()} of ID {item_id} deleted")
    else:
        print(f"Deletion of {desc} of ID {item_id} failed")
