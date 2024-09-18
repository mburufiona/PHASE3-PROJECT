# import functions from the contact file
from contact import (
    add_contact,
    view_contacts,
    search_contact,
    edit_contact,
    delete_contact
)
def main():
    # Main loop for the contact book
    while True:
        # Display the menu options
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        # Get user input for menu choice
        choice = int(input("Enter your choice: "))

        # option to add a new contact
        if choice == 1:
            name = input("Enter name: ") # prompt for name
            phone = input("Enter phone: ") # prompt for phone
            email = input("Enter email: ") # prompt for email
            add_contact(name, phone, email) # call function to add the contact
            print("Contact added!") # Confirmation message

        # option to view all contacts
        elif choice == 2:
            contacts = view_contacts() # Retrieve all contacts
            for contact in contacts: # loop and display each contact
                print(contact)

        # option to search for contacts
        elif choice == 3:
            name = input("Enter name: ") # prompt for name to search
            contacts = search_contact(name) # call function to search for contacts
            for contact in contacts: # loop and display found contact
                print(contact)

        # Option to edit an existing contact
        elif choice == 4:
            contact_id = int(input("Enter contact id: "))
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            edit_contact(contact_id, name, phone, email) # call function to update the contact
            print("Contact updated!")

        # Option to delete a contact
        elif choice == 5:
            contact_id = int(input("Enter contact id: "))
            delete_contact(contact_id) # call function to delete contact
            print("Contact deleted!")

        # option to exit the program
        elif choice == 6:
            print("Exit...")
            break

        else:
            print("Invalid choice. PLease try again") # E rror message for invalid choices

# Entry point of the program
if __name__ == "__main__":
    main() # call the main function to run the program