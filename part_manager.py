from tkinter import *
from db import Database

db = Database('store.db')


# Populate the list view with data
def populate_list():
    for row in db.fetch():
        parts_list.insert(END, row)


# Add an item
def add_item():
    print('Add')


# Remove an item
def remove_item():
    print('Remove')


# Update an item
def update_item():
    print('Update')


# Clear text for item input
def clear_text():
    print('Clear')


# Create window
app = Tk()

# price
part_text = StringVar()
part_label = Label(app, text='Part Name', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# Customer
customer_text = StringVar()
customer_label = Label(app, text='Customer', font=('bold', 14))
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

# Retailer
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer', font=('bold', 14), pady=20)
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)

# Price
price_text = StringVar()
price_label = Label(app, text='Price', font=('bold', 14), pady=20)
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

# Parts List (Listbox)
parts_list = Listbox(app, height=8, width=50, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Scrollbar for above Listbox
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

# Set scroll to above Listbox
parts_list.configure(yscrollcomman=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

# Button for add part item
add_btn = Button(app, text="Add Part", width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

# Button for remove part item
remove_btn = Button(app, text="Remove Part", width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

# Button for updating part item
update_btn = Button(app, text="Update Part", width=12, command=update_item)
update_btn.grid(row=2, column=2)

# Buttons for clearing item input
clear_btn = Button(app, text="Clear Input", width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

# Title and window width/height
app.title('Price Manager')
app.geometry('700x350')

# Populate data
populate_list()

# Start program
app.mainloop()
