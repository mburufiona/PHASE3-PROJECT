import sqlite3

class ContactManager:
    def __init__(self, db_name='contacts.db'): # Initialize the contact manager instance with database name
        self.db_name = db_name
        # This creates the contacts table in the database if its not there
        self.create_table()

    def create_table(self):
        # connects to the database
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            ''')
            conn.commit() # commit changes to the database

    def add_contact(self, name, phone, email):
        with sqlite3.connect(self.db_name) as conn: # Add a new contact to the database
            cursor = conn.cursor()
            cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
            conn.commit()

    def view_contacts(self):
        # Retrieve all contacts from the database
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contacts")
            return cursor.fetchall()

    def search_contact(self, name):
        # search contacts by name
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + name + '%',))
            # Returns a matching contact
            return cursor.fetchall()

    def edit_contact(self, contact_id, name, phone, email):
        # Update a contact in the database
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE contacts SET name = ?, phone = ?, email = ? WHERE id = ?", (name, phone, email, contact_id))
            conn.commit()

    def delete_contact(self, contact_id):
        # Delete a contact from the database
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
            # commit the changes to the database
            conn.commit()

