from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


root = Tk()
root.title("To-do List Application")
icon = PhotoImage(file="Images/icon.png")
root.iconphoto(False,icon)
root.config(bg='#b6d0e2')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 600
window_height = 530
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

task_input_placeholder = 'Type a task...'
#background_image = Image.open("SP.jpg")
#bg_photo = ImagePhotoImage(background_image)
#background_label = Label(root, image=bg_photo)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

def add_task():
    task = task_input.get()
    if task != task_input_placeholder and task != '':
        task_no = task_list.size() + 1
        task_update = f"{task_no}.{task}"
        task_list.insert(END, task_update)
        task_input.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)

        for i in range(task_list.size()):
            task = task_list.get(i).split('.',1)[1]
            task_list.delete(i)
            task_list.insert(i,f"{i+1}.{task}")
    except:
        messagebox.showwarning("Warning", "Select a task to delete.")

def task_mark():
    try:
        selected_task_index = task_list.curselection()[0]
        task = task_list.get(selected_task_index)
        task_list.delete(selected_task_index)
        completed_task = f"[Done] {task}"
        task_list.insert(selected_task_index, completed_task)
    except:
        messagebox.showwarning("Warning", "Select a task to mark as completed.")

title_label = Label(root, text="My To-Do List", font=('Times New Roman', 20, 'bold'), bg='#b6d0e2')
title_label.pack(pady=15)

main_frame = Frame(root, bg='#b6d0e2')
main_frame.pack()

task_input = Entry(main_frame, width=40, font=('Times New Roman', 14))
task_input.insert(0, task_input_placeholder)
task_input.bind("<FocusIn>",
                lambda args: task_input.delete('0', END) if task_input.get() == task_input_placeholder else None)
task_input.bind("<FocusOut>",
                lambda args: task_input.insert('0', task_input_placeholder) if task_input.get() == '' else None)
task_input.grid(row=0, column=1, padx=10,pady=0,sticky='w')

def on_add(e):
    add_button.config(image=hover_image1)

def off_add(e):
    add_button.config(image=normal_image1)

normal_image1 = PhotoImage(file="Images/add_dark_btn.png")
hover_image1 = PhotoImage(file="Images/add_btn.png")

add_icon = ImageTk.PhotoImage(Image.open('Images/add_dark_btn.png'))
add_button = Button(main_frame, image=add_icon,bg='#b6d0e2',border=0, command=add_task)
add_button.grid(row=0, column=2, padx=10)

add_button.bind("<Enter>", on_add)
add_button.bind("<Leave>", off_add)

def on_delete(e):
    delete_button.config(image=hover_image2)
def off_delete(e):
    delete_button.config(image=normal_image2)

normal_image2 = PhotoImage(file="Images/delete_dark_btn.png")
hover_image2 = PhotoImage(file="Images/delete_btn1.png")

del_label = Label(main_frame,background='#b6d0e2',text="Hit Delete",font=('Times New Roman',15))
del_label.grid(row=1,column=0,sticky='e')
del_icon = ImageTk.PhotoImage(Image.open('Images/delete_dark_btn.png'))
delete_button = Button(main_frame,image=del_icon,bg='#b6d0e2',border=0, command=delete_task)
delete_button.grid(row=1, column=1,sticky='w')

delete_button.bind("<Enter>", on_delete)
delete_button.bind("<Leave>", off_delete)

def on_mark(e):
   mark_button.config(image=hover_image3)

def off_mark(e):
    mark_button.config(image=normal_image3)

normal_image3 = PhotoImage(file="Images/done_dark_btn.png")
hover_image3 = PhotoImage(file="Images/done_btn1.png")

mark_label = Label(main_frame,text="Hit Done",bg='#b6d0e2',font=('Times New Roman',15))
mark_label.grid(row=1,column=1,sticky='e')
mark_icon = ImageTk.PhotoImage(Image.open('Images/done_dark_btn.png'))
mark_button = Button(main_frame,image=mark_icon,bg='#b6d0e2',  bd=0, command=task_mark)
mark_button.grid(row=1, column=2, sticky='w')

mark_button.bind("<Enter>", on_mark)
mark_button.bind("<Leave>", off_mark)

task_list_frame = Frame(root)
task_list_frame.pack(pady=20)

task_list = Listbox(task_list_frame, width=50, height=15, font=('Times New Roman', 14), selectbackground='#a1c5e2')
task_list.pack(side=LEFT, fill=BOTH, padx=(0, 10))

scrollbar = Scrollbar(task_list_frame)
scrollbar.pack(side=RIGHT, fill=Y)

task_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_list.yview)

root.bind('<Return>', lambda event: add_task())

root.mainloop()
