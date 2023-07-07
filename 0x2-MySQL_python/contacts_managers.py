import mysql.connector
import os

DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD") 

database_connection = mysql.connector.connect(
    host="localhost",
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    database="contacts"
)

def create_contact(name, email, phone):
    if not name or not email:
        print("Name and email are required:")
        return

    cursor = database_connection.cursor()
    query = "INSERT INTO contacts (name, email, phone) VALUES (%s, %s, %s)"
    values = (name, email, phone)
    cursor.execute(query, values)
    database_connection.commit()
    cursor.close()
# create_contact("Joseph", "nchimunya@gmail.com", "+260977398719")

def get_all_contacts():
    cursor = database_connection.cursor()
    query = "SELECT * FROM contacts"
    cursor.execute(query)
    contacts = []
    for row in cursor.fetchall():
        contact = {
            "name": row[1],
            "email": row[2],
            "phone": row[3]

        }
        contacts.append(contact)
    cursor.close()
    return contacts

#update the contacts
def update_contact(contact_id, name, email, phone):
    if not name or not email:
        print("Name and email are required:")
        return


    cursor = database_connection.cursor()
    query = "UPDATE contacts SET name=%s, email=%s, phone=%s WHERE id=%s"
    values = (name, email, phone, contact_id)
    cursor.execute(query, values)
    database_connection.commit()
    cursor.close()

#Delete a user
def delete_contact(contact_id):
    cursor = database_connection.cursor()
    query = "DELETE FROM contacts WHERE id=%s"
    values = (contact_id),
    cursor.execute(query, values)
    database_connection.commit()
    cursor.close()

#Get a single User
def get_single_user(contact_id):
    cursor = database_connection.cursor()
    query = "SELECT * FROM contacts WHERE id=%s"
    values = (contact_id),
    cursor.execute(query, values)
    rows = cursor.fetchone()
    cursor.close()
    return rows

delete_contact(5)
contact = get_single_user(2)
print(contact)

contacts = get_all_contacts()
for contacts in contacts:
     print(contacts)


create_contact("Joseph", "nchimunya@gmail.com", "+260977398719")
update_contact(2, "Sharoon","sharonmwale@gmail.com", "+260977809777")