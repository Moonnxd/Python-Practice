items = []

while True:
    print("------ Inventory System ------")
    print("[1] Add Item")
    print("[2] View Items")
    print("[3] Search Item")
    print("[4] Remove Item")
    print("[5] Exit")
    print("------------------------------")
    
    choice = int(input("Choice: "))

    if(choice == 1):
        print("\n------ Add Item ------")
        addItem = input("Enter Item to add: ")

        for item in items:
            if item.lower() == addItem.lower():
                print()
                print("Item is already in inventory.")
                print()
                break

        else:
            items.append(addItem)
            print()
            print(addItem, "added successfully!")
            print()

    elif(choice == 2):
        print()
        print("------ Items ------")

        for item in items:
            print("-", item)

        print("-------------------")
        print()
        continue

    elif(choice == 3):
        print()
        print("------ Search Item ------")
        searchItem = input("Enter Item to search: ")

        for item in items:
            if item.lower() == searchItem.lower():
                print()
                print(searchItem, "is in inventory.")
                print()
                break

        else:
            print()
            print(searchItem, "is not on inventory.")
            print()

    elif(choice == 4):
        print()
        print("------ Remove Item ------")
        removeItem = input("Enter item to remove: ")

        for item in items:
            if item.lower() == removeItem.lower():
                items.remove(item)
                print()
                print(removeItem, "removed successfully!")
                print()
                break

        else:
            print()
            print("Item is not on inventory.")
            print()

    elif(choice == 5):
        print()
        print("Program Closed.")
        print()
        break

    else:
        print()
        print("Invalid Choice.")
        print()