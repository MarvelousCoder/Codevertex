from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Contact"
)
cursor = mydb.cursor()

def get_all_contacts():
    try:

        cursor.execute('SELECT * FROM contact_details')
        rows = cursor.fetchall()
        return rows
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
root = Tk()
root.title("Contack Book")
icon = PhotoImage(file="Images/icon.png")
root.iconphoto(False,icon)
root.configure(bg="#FFEBCD")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 600
window_height = 530
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

def submit_data():
    name_value = name_entry.get()
    phone_value = phone_entry.get()
    email_value = email_entry.get()
    address_value = address_entry.get()

    if not name_value or not phone_value or not email_value or not address_value:
        messagebox.showerror("Input error","Insert all data")
        return

    try:
        cursor = mydb.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS contact_details (Name VARCHAR(20), Phone_no VARCHAR(10), Email VARCHAR(20), Address VARCHAR(30))")
        query = "INSERT INTO contact_details (Name, Phone_no, Email, Address) VALUES (%s, %s, %s,%s)"
        cursor.execute(query,(name_value,phone_value,email_value,address_value))
        mydb.commit()
        messagebox.showinfo("Success","Data inserted successfully")
        #print(my_cursor.rowcount, "Records inserted.")
        name_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        address_entry.delete(0, 'end')

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        messagebox.showerror("Error", "Error occurred")

def view_contacts():
    for item in tree.get_children():
        tree.delete(item)
    contacts = get_all_contacts()
    for contact in contacts:
        tree.insert('', 'end', values=contact)

def on_tree_select():
    selected_item = tree.focus()
    if selected_item:
        values = tree.item(selected_item, 'values')
        #global selected_contact_name
        #selected_contact_name = values[0]
        name.set(values[0])
        phone.set(values[1])
        email.set(values[2])
        address.set(values[3])

def delete_contact():
    try:
        selected_item = tree.focus()
        if selected_item:
            values = tree.item(selected_item, 'values')
            query = "DELETE FROM contact_details WHERE Name = %s AND Phone_no = %s AND Email = %s AND Address = %s"
            cursor.execute(query, (values[0], values[1], values[2], values[3]))
            mydb.commit()
            tree.delete(selected_item)
            messagebox.showinfo("Success", "Contact deleted successfully")
            name_entry.delete(0, 'end')
            phone_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            address_entry.delete(0, 'end')
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        messagebox.showerror("Error", "Error occurred")

background_color = '#f0f0f0'
accent_color = '#3498db'
text_color = '#333'
font_style = ('Times New Roman', 10)

entry_style = ttk.Style()
entry_style.configure('TEntry', font=font_style, foreground=text_color, background=background_color, borderwidth=1, relief='solid')

name = StringVar()
name_label = Label(root,text="Name",bg="#FFEBCD")
name_label.grid(row=0,column=0,sticky='e',padx=10,pady=10)
name_entry = ttk.Entry(root,width=30,font=font_style,style='TEntry', textvariable=name)
name_entry.grid(row=0,column=1,padx=10,pady=10)

phone = StringVar()
phone_label = Label(root,text="Phone no ",bg="#FFEBCD")
phone_label.grid(row=1,column=0,sticky='e',padx=10,pady=10)
phone_entry = ttk.Entry(root,width=30,font=font_style,style='TEntry',textvariable=phone)
phone_entry.grid(row=1,column=1,padx=10,pady=10)

email = StringVar()
email_label = Label(root,text="Email ID",bg="#FFEBCD")
email_label.grid(row=2,column=0,sticky='e',padx=10,pady=10)
email_entry = ttk.Entry(root,width=30,font=font_style,style='TEntry', textvariable=email)
email_entry.grid(row=2,column=1,padx=10,pady=10)

address = StringVar()
address_label = Label(root,text="Address",bg="#FFEBCD")
address_label.grid(row=3,column=0,sticky='e',padx=10,pady=10)
address_entry = ttk.Entry(root,width=30,font=font_style,style='TEntry',textvariable=address)
address_entry.grid(row=3,column=1,padx=10,pady=10)

button_style = ttk.Style()
button_style.configure('TButton',font=font_style,foreground =text_color,background_color = accent_color)

submit_btn = ttk.Button(root, text="Submit",style='TButton',command=submit_data)
submit_btn.grid(row=0,column=4)
root.bind('<Return>', lambda event: submit_data())

view_btn = ttk.Button(root, text="View Contacts",style='TButton', width=15, command=lambda: view_contacts()).grid(row=1, column=4, padx=5)
del_btn = ttk.Button(root, text="Delete Contact",style='TButton', command=lambda:delete_contact()).grid(row=2, column=4,padx=5)

tree_style = ttk.Style()
tree_style.configure('Treeview', font=font_style, foreground=text_color, background=background_color, rowheight=25)
tree_style.configure('Treeview.Heading', font=font_style, foreground=text_color, background=accent_color)

columns = ('name', 'phone', 'email', 'address')
tree = ttk.Treeview(root, columns=columns, show='headings',style='Treeview')
tree.heading('name', text='Name')
tree.heading('phone', text='Phone')
tree.heading('email', text='Email')
tree.heading('address', text='Address')

tree.column('name', width=100)
tree.column('phone', width=100)
tree.column('email', width=100)
tree.column('address', width=150)

tree.grid(row=5, column=0, columnspan=5, padx=10, pady=10, sticky='nsew')

scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=5, column=5, sticky='ns')

root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(1, weight=1)

tree.bind('<<TreeviewSelect>>', lambda event: on_tree_select())

root.mainloop()