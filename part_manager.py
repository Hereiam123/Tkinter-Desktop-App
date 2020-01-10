from tkinter import *

# Create window
app = Tk()

# price
price_text = StringVar()
price_label = Label(app, text='price Name', font=('bold', 14), pady=20)
price_label.grid(row=0, column=0, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=0, column=1)

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

# Title and window width/height
app.title('price Manager')
app.geometry('700x350')


# Start program
app.mainloop()
