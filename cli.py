from contact import (
    add_contact,
    view_contacts,
    search_contact,
    edit_contact,
    delete_contact
)
def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
            print("Contact added!")

        elif choice == 2:
            contacts = view_contacts()
            for contact in contacts:
                print(contact)

        elif choice == 3:
            name = input("Enter name: ")
            contacts = search_contact(name)
            for contact in contacts:
                print(contact)

        elif choice == 4:
            contact_id = int(input("Enter contact id: "))
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            edit_contact(contact_id, name, phone, email)
            print("Contact updated!")

        elif choice == 5:
            contact_id = int(input("Enter contact id: "))
            delete_contact(contact_id)
            print("Contact deleted!")

        elif choice == 6:
            print("Exit...")
            break

        else:
            print("Invalid choice. PLease try again")

if __name__ == "__main__":
    main()