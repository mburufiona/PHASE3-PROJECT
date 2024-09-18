import sqlite3

# Function to add a new contact to the database
def add_contact(name, phone, email):
    # Connect to the SQLite database 
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor() # Create a cursor object to execute SQL commands
    # Insert the new contact into the 'contacts' table
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit() # Commit the transaction to save changes
    conn.close() # Close the database connection
    

# Function to view all contacts in the database
def view_contacts():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts") # Execute a query to select all contacts
    contacts = cursor.fetchall() # Fetch all results from the query
    conn.close()
    return contacts # Return the list of contacts

# Function to search for contacts by name
def search_contact(name):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    # Execute a query to select contacts whose name match the search term
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + name + '%',))
    contact = cursor.fetchall() # Fetch all matching contacts
    conn.close()
    return contact # Return the list of matching contacts

# Function to edit an existing contact
def edit_contact(contact_id, name, phone, email):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    # Update the contact's details in the database based on the contact ID
    cursor.execute("UPDATE contacts SET name = ?, phone = ?, email = ? WHERE id = ?", (name, phone, email, contact_id))
    conn.commit() # Commit changes to database
    conn.close() # close database connection

# Function to delete a contact from the database
def delete_contact(contact_id):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    # Execute to query to delete the contact based on the contact ID
    cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
    conn.commit()
    conn.close()