
# Main menu
def mainMenu():

    # Menu
    print("___________________________")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("Select Options From Below: ")
    print("___________________________")
    print("1 - Add Inventory Items    |")
    print("2 - View Current Inventory |")
    print("___________________________|")

# Choices
    while True:
        decision = input("Select 1 or 2: ")
        if decision == "1":
            addingToInventory()
            break
        elif decision == "2":
            viewInventory()
            break
        elif decision != "1" or "2":
            print("Invalid Option Try Again")

# Menu to add Item name and amount
def addingToInventory():

    # Menu
    print("___________________")
    print("ADD INVENTORY ITEMS")
    print("___________________")
    print()
    print("1 - Add Items")
    print("B - Return to Menu")
    print()

    # Adds Inventory Items
    while True:
        decision = input("Choose An Option: ")
        if decision in ['1', 'b']:
            break
    if decision == "1":
        print()
        while True:
            numberOfItems = input("Enter the Number of Items to be Added: ")
            if numberOfItems.isdigit():
                break
        numberOfItems = int(numberOfItems)
        itemNames = {}
        for i in range(1, numberOfItems + 1):
            while True:
                print("______________")
                itemName = input("Item Name: ")
                if itemName != '':
                    break
            while True:
                itemValue = input("Item Amount: ")
                if itemValue.isdigit():
                    break
            # stores inputs into text file
            itemNames.update({itemName: int(itemValue)})
            addingToTextFile(itemNames, clear=False)
            returnToMenu("Item/s Have Been Added")
    # returns to menu
    elif decision == "b":
        print()
        returnToMenu("Returning to Menu")

# Views the current Inventory with the option to edit and delete
def viewInventory():
    # Menu
    print("_________________________")
    print("CURRENT INVENTORY STORAGE")
    print("_________________________")
    print()
    items = retrieveItems()
    for item in items:
        print(f"{item}: {items[item]}")    # draws and prints from file

    print("AVAILABLE OPTIONS: ")
    print("__________________ ")
    print("1 - Edit Item")
    print("2 - Remove Item")
    print("b - Return to Menu")
    print("__________________ ")
    print()

    # Options to select from
    while True:
        decision = input("Select An Option: ")
        if decision == '1':
            editItems()
            break
        elif decision == '2':
            deleteItems()
            break
        elif decision == 'b':
            print()
            returnToMenu("Returning to Menu")

# Function that allows to edit variables within the text file
def editItems():
    # Menu
    print("_____________________")
    print("EDIT INVENTORY ITEM/S")
    print("_____________________")
    print()
    print("AVAILABLE OPTIONS: ")
    print()
    print("1 - Edit Item Name")
    print("2 - Edit Item Amount")
    print("_____________________")

    # Loop breaks if value is 1 or 2
    while True:
        decision = input("Choose An Option: ")
        if decision in ["1", "2", "b"]:
            break

    # Option 1
    itemNames = retrieveItems()
    if decision == '1':
        print()
        while True:
            itemBeingEdited = input("Enter Name to Edit: ")
            if itemBeingEdited in itemNames:
                break
            else:
                print("Value Incorrect, Item/s Don't Exist")
                print("______________________")
        while True:
            newItemName = input("Enter New Item: ")
            if newItemName != '':
                break
        itemNames.update({newItemName: itemNames[itemBeingEdited]})
        del itemNames[itemBeingEdited]

        addingToTextFile(itemNames, clear=True)
        returnToMenu("Item has been Edited")

    # Option 2
    elif decision == '2':
        print()
        while True:
            itemBeingEdited = input("Enter Name to Edit: ")
            if itemBeingEdited in itemNames:
                break
            else:
                print("Items Does Not Exist")
                print("____________________")
        while True:
            newItemAmount = input("Enter New Item Amount: ")
            if newItemAmount.isdigit():
                break

        # stores inputs into text file
        itemNames.update({itemBeingEdited: newItemAmount})
        addingToTextFile(itemNames, clear=True)
        returnToMenu("New Item Value added")

    # Returns to Menu
    elif decision == 'b':
        print()
        returnToMenu("Returning to Menu")

# Deletes items in text file
def deleteItems():

    # Menu
    print("_____________________")
    print("DELETE INVENTORY ITEM")
    print("_____________________")

    # Method for selecting and deleting item
    itemNames = retrieveItems()
    while True:
        itemBeingDeleted = input("Enter Name to Delete: ")
        print("_____________________")
        if itemBeingDeleted != "":
            del itemNames[itemBeingDeleted]
            addingToTextFile(itemNames, clear=True)
            returnToMenu("Item Deleted")
            break
        else:
            print("That Item Does Not Exist")
            print()


# Opens File
def addingToTextFile(ItemNames: dict, clear: bool):
    if clear:
        f = open("Inventory.txt", "w")
        f.close()
        with open("Inventory.txt", "a") as file:
            for item in ItemNames:
                file.write(f"{item}: {ItemNames[item]}")
        return

# Adds Items to text file
    invItems = retrieveItems()
    for item in invItems:
        if item in ItemNames:
            ItemNames[item] += invItems[item]

    with open("Inventory.txt", "a") as file:
        for item in ItemNames:
            file.write(f"{item}: {ItemNames[item]}")

# Selects the item within text file
def retrieveItems():
    itemNames={}
    with open('Inventory.txt', 'r') as file:
        for line in file:
            line = line.replace('\n', '').split(':')
            itemName, itemAmount = line[0], line[1].strip()
            itemNames.update({itemName: int(itemAmount)})
    return itemNames

# Function to return to the first menu
def returnToMenu(message):
    while True:
        print()
        menu = input(f"{message}. Press B for the Main Menu: ")
        if menu == 'b':
            mainMenu()
            break

mainMenu()

