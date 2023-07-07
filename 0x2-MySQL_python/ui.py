import tkinter as tk
from tkinter import messagebox
from functools import partial

#import the CRUD functions
from contacts_managers import create_contact, get_all_contacts, update_contact, delete_contact

#create the main application window 
window = tk.Tk()
window.title("Address Book")

#Create labels and entry fields
label_name = tk.Label(window, text="Name:")
entry_name = tk.Entry(window)

label_email = tk.Label(window, text="Email:")
entry_email = tk.Entry(window)

label_phone = tk.Label(window, text="Phone:")
entry_phone = tk.Entry(window)

#Create a listbox to display contacts
contact_listbox = tk.Listbox(window, width=50)

#Function to populate the listbox withcontacts
def load_contacts():
    contact_listbox.delete(0, tk.END)
    contacts = get_all_contacts()
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['email']} - {contact['phone']}")

#Function to add a new contact
def add_contact():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    create_contact(name, email, phone)
    load_contacts()
    messagebox.showinfo("Sucess", "Contact added Sucessfully.")

    #Function to update a contact
def update_selected_contact():
     selected_index = contact_listbox.curselection()
     if selected_index:
        contact_id = selected_index[0] + 1
        name = entry_name.get()
        email = entry_email.get()
        phone = entry_phone.get()
        update_contact(contact_id, name, email, phone)
        load_contacts()
        messagebox.showerror("Sucess", "Contact updated Sucessfully.")
     else:
        messagebox.showinfo("Error", "No contact selected.")

#Function to delete a contact
def delete_selected_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        contact_id = selected_index[0] + 1
        delete_contact(contact_id)
        load_contacts()
        messagebox.showerror("Sucess", "Contact deleted Sucessfully.")
    else:
        messagebox.showinfo("Error", "No contact selected.")

#Set the layout of the UI elements
label_name.pack()
entry_name.pack()

label_email.pack()
entry_email.pack()

label_phone.pack()
entry_phone.pack()

contact_listbox.pack()

button_add = tk.Button(window, text="Add Contact", command=add_contact)
button_update = tk.Button(window, text="Update Contact", command=update_selected_contact)
button_delete = tk.Button(window, text="Delete Contact", command=delete_selected_contact)

button_add.pack()
button_update.pack()
button_delete.pack()

#Load contacts on application startup
load_contacts()

#Start the main even loop
window.mainloop()
