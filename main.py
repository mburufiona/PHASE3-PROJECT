# Import the contactManager class from contact_manager module
from contact_manager import ContactManager

def main():
    manager = ContactManager()  # Initialize the contact manager

    while True:
        # print the menu options
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        # get the user's choice
        choice = int(input("Enter your choice: "))

        # Handle the user's choice
        if choice == 1:
            # add a new contact
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            manager.add_contact(name, phone, email)
            print("Contact added!")

        elif choice == 2:
            # view all contacts
            contacts = manager.view_contacts()
            for contact in contacts:
                print(contact)

        elif choice == 3:
            # search contacts by name
            name = input("Enter name: ")
            contacts = manager.search_contact(name)
            for contact in contacts:
                print(contact)

        elif choice == 4:
            # edit an existing contact
            contact_id = int(input("Enter contact id: "))
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            manager.edit_contact(contact_id, name, phone, email)
            print("Contact updated!")

        elif choice == 5:
            # delete a contact
            contact_id = int(input("Enter contact id: "))
            manager.delete_contact(contact_id)
            print("Contact deleted!")

        elif choice == 6:
            # exit the program
            print("Exit...Bye")
            break

        else:
            # this handle invalid input
            print("Invalid choice. Please try again.")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
