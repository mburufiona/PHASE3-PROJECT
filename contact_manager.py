import sqlite3

class ContactManager:
    def __init__(self, db_name='contacts.db'):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
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
            conn.commit()

    def add_contact(self, name, phone, email):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
            conn.commit()

    def view_contacts(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contacts")
            return cursor.fetchall()

    def search_contact(self, name):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + name + '%',))
            return cursor.fetchall()

    def edit_contact(self, contact_id, name, phone, email):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE contacts SET name = ?, phone = ?, email = ? WHERE id = ?", (name, phone, email, contact_id))
            conn.commit()

    def delete_contact(self, contact_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
            conn.commit()
