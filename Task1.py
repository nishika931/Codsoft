# contact book
contacts = []

# function for adding name
def add_contact():
    name = input("enter name:")
    phone_num =input("enter phone number:")
    email = input("enter email:")
    address = input("enter address:")

    contact = {
        "name": name,
        "phone number": phone_num,
        "email": email,
        "address": address,
    }
    contacts.append(contact)
    print(" contact has been added to your contact book.\n")

# function to view contacts
def view_contact():
    if len(contacts) == 0:
        print("No contact found\n")
    else:
        print("contact list:")
        i = 1
        for contact in contacts:
            print(i, " name", contact["name"])
            print("   phone number", contact["phone number"])
            print("   email", contact["email"])
            print("   address", contact["address"])
            print("----------*----------")
            i += 1

# function for searching contacts
def search_contact():
    value = input("enter name or phone number which you want to search:")
    for contact in contacts:
        if contact["name"] == value or str(contact["phone number"]) == value:
            print("contact found.")
            print("name", contact["name"])
            print("phone number", contact["phone number"])
            print("email", contact["email"])
            print("address", contact["address"])
            print("----------*----------")
            return
    print("Not found.\n")

# function for update contacts
def update_contact():
    value = input("enter name or phone number to update:")
    for contact in contacts:
        if contact["name"] == value or str(contact["phone number"]) == value:
            print("contact found .Please enter new detail to update:")
            contact["name"] = input("enter new name:")
            contact["phone number"] = input("enter new phone number:")
            contact["email"] = input("enter new email:")
            contact["address"] = input("enter new address:")
            print("contact updated.\n")
            return
    print("contact not found")

# function for deleting contacts
def delete_contact():
    value = input("enter name or phone number you want to delete:")
    for contact in contacts:
        if contact["name"] == value or str(contact["phone number"]) == value:
            contacts.remove(contact)
            print("contact deleted successfully.\n")
            return
    print("contact not found.\n")

# main loop
while True:
    print("contact book\n")
    print("contact book menu:\n")
    print("add-to add contacts")
    print("view-to view contacts")
    print("search-to search contacts")
    print("update-to update contacts")
    print("delete-to delete contacts")
    print("exit-to exit")

    choice = input("enter your choice:").lower()
    if choice == "add":
        add_contact()
    elif choice == "view":
        view_contact()
    elif choice == "search":
        search_contact()
    elif choice == "update":
        update_contact()
    elif choice == "delete":
        delete_contact()
    elif choice == "exit":
        print("Thanks.")
        break
    else:
        print("Invalid choice . Please try again \n")