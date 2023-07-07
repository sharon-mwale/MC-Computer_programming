from tkinter import Tk
from ui import AddressBookUI

#Entry point of the application
if __name__ == "__main__":
    #Create the Tkinter root window
    root = Tk()
    root.title("Address Book")

    #Create an instance of the AddressBookUI
    address_book_ui = AddressBookUI(root)

    #Start the Tkinter even loop
    root.mainloop()