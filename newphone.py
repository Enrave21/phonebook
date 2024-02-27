import sqlite3

# Function to create the contact table if it doesn't exist
def create_table():
    conn = sqlite3.connect('contacts.db')
    #c = conn.cursor()
    conn.execute('''CREATE TABLE IF NOT EXISTS contacts(
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(30), 
                    phone BIGINT UNSIGNED,
                    email VARCHAR(30))''')
    conn.commit()
    conn.close()

# Function to add a new contact
def add_contact(name, phone, email):
    conn = sqlite3.connect('contacts.db')
    #c = conn.cursor()
    conn.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()
    print("Contact added successfully.")

# Function to display all contacts
def display_contacts():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    contacts = c.fetchall()
    print("Contacts:")
    for contact in contacts:
        print(f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}")
    conn.close()

# Function to delete a contact
def delete_contact(contact_id):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    conn.close()
    print("Contact deleted successfully.")

# Main function
def main():
    create_table()
    while True:
        print("\n1. Add Contact")
        print("2. Display Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            add_contact(name, phone, email)
        elif choice == '2':
            display_contacts()
        elif choice == '3':
            contact_id = input("Enter the ID of the contact to delete: ")
            delete_contact(contact_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()