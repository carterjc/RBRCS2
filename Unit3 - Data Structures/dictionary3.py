# Carter Costic
# 31/Oct/19

import random
# Create a dictionary ‘groceryStore’ that contains a dictionary of 5
# items
# 	groceryStore keys will be numbers
# 	Dictionary items will have k/v pairs that include:
# 		‘itemName’: ‘apple’,
# 		‘itemPrice’: 6,
# 		‘itemQuant’: 10


groceryStore = {}
items = [("apple", 4.99, 17), ("orange", 2.95, 34), ("banana", 13.87, 67), ("dog", 459.95, 10), ("cat", 1.00, 1000)]
for item in items:
    groceryStore[item[0]] = {
        "itemPrice": item[1],
        "itemQuant": item[2]
    }


# Create a variable ‘grandTotal’ to hold the value of each item as we # compile them into a shopping cart
grandTotal = 0

# Create a list ‘shoppingCart’ that will store our items being
# purchased
shoppingCart = []

# Create a function ‘addToCart’ that will take in items we wish to add
# to our cart.

print("Welcome to Store! A store that provides item at a cost.\n\n--------\n")


def printShoppingInv(inventory):
    for index in inventory:
        print(index[0])


def condenseShopList():
    listOfItems = []
    duplicateItems = []
    newList = []
    for item in shoppingCart:
        listOfItems.append(item[0])
        if item[0] in listOfItems and item[0] not in duplicateItems:
            duplicateItems.append(item[0])
            newQuant = 0
            for obj in shoppingCart:
                if obj[0] == item[0]:
                    newQuant += obj[1]
            newList.append((item[0], newQuant))
    return newList


def checkout():
    print("\n------Receipt------\n")
    for i in condenseShopList():
        print(i[0].capitalize() + "s: " + str('${:,.2f}'.format(groceryStore[i[0]]["itemPrice"])) + " x " + str(i[1]))
    print("Your total is " + str('${:,.2f}'.format(grandTotal)) + ".")
    print("\n------Receipt------")
    print("\nThank you for shopping with us!")


def addToCart(item, num):
    if item in groceryStore:
        if groceryStore[item]["itemQuant"] >= num:
            groceryStore[item]["itemQuant"] -= num
            shoppingCart.append((item, num))
            global grandTotal
            grandTotal += groceryStore[item]["itemPrice"] * num
            if num == 1:
                print("You added 1 " + item + ".")
            else:
                print("You added " + str(num) + " " + item + "s.")
        else:
            print("Sorry, there is not enough stock. Try again with a smaller quantity.")
    else:
        print("Sorry, this item is not in the store. Please try again")


shopping = True
while shopping:
    shopping = str(input("Do you want to purchase an item? (Y/N)"))
    if shopping == "N":
        shopping = False
        break
    elif shopping == "Y":
        inventory = "\nChoose from our massive selection of items!\n\n"
        for index in items:
            inventory += "{} priced at {} - [{} remaining]\n".format(index[0].capitalize() + "s", '${:,.2f}'.format(index[1]), groceryStore[index[0]]["itemQuant"])
        print(inventory)
        itemNum = int(input("Enter the number of the item you want above. (Ex. Apples - 1)")) - 1
        if itemNum < len(items):
            item = items[itemNum][0]
            print("There are " + str(groceryStore[item]["itemQuant"]) + " " + item + "s left in stock.")
            itemQuant = input("Enter the number you want to purchase.")
            if str(itemQuant).isdigit():
                addToCart(item, itemQuant)
            else:
                print("That is not a valid quantity.")


if grandTotal > 0:
    checkout()
else:
    print("\nSorry to see you go. Thanks for visiting!")
