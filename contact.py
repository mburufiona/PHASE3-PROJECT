import sqlite3

def add_contact(name, phone, email):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()
    

def view_contacts():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    conn.close()
    return contacts

def search_contact(name):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' +name, + '%'))
    contact = cursor.fetchall()
    conn.close()
    return contact

def edit_contact(contact_id, name, phone, email):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE contacts SET name = ?, phone = ?, email = ? WHERE id = ?", (name, phone, email, contact_id))
    conn.commit()
    conn.close()

def delete_contact(contact_id):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
    conn.commit()
    conn.close()