contact = {}

def dispay():
    print("\n\nContact Lists:\n Name \t Contact")
    for key in contact:
        print("{} \t {}".format(key, contact.get(key)))

while True:
    choice =int( input("1. Add New Contact\n"
                   "2. Search the Contact\n"
                   "3. Display the Contact\n"
                   "4. Edit the Contact\n"
                   "5. Delete the Contact\n"
                   "6. Exit\n"
                   "Choice your option: "))

    match choice:
        case 1:
            name = input("Add Your Contact Name: ")
            phone = input("Add Your Contact Number: ")
            contact[name] = phone
            dispay()

        case 2:
            contactName = input("Search the Contact: ")
            if contactName in contact:
                print(contactName, "    Number: ",contact[contactName])
            else:
                print(contactName, " is not exist!")

        case 3:
            if not contact:
                print("Contact Book is empty!")
            else:
                dispay()

        case 4:
            editContact = input("Enter Contact Name: ")
            if editContact in contact:
                phone = input("Edit Your Number: ")
                contact[editContact] = phone
                print("Contact Updated Successfully")
                dispay()
            else:
                print("Contact Name is not found!")

        case 5:
            deleteContact = input("Which Contact Do You Want to Delete?: ")
            if deleteContact in contact:
                deleteConfirm = input("Do you want to delete this contact? [y/n]: ")
                if deleteConfirm == "Y" or deleteConfirm == "y":
                    contact.pop(deleteContact)
                    dispay()
            else:
                print("The name is not found in the contact!")

        case 6:
            exit(0)

        case _:
            print("Invalid Choice!")

    print("\n")
