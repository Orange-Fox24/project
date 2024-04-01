import os
from tkinter import messagebox, ttk
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext
from PIL import ImageTk, Image
import datetime
import requests
from deep_translator import GoogleTranslator
from io import BytesIO


def next_page():
    global root1, bg_image
    root1.destroy()
    root2 = tk.Tk()
    root2.title("Умный Холодильник!")
    root2.geometry("1300x600")

    icon1 = ImageTk.PhotoImage(file='Subtract (1).png')
    root2.wm_iconbitmap()
    root2.iconphoto(False, icon1)

    image1 = Image.open("fon.png")
    bg_image = ImageTk.PhotoImage(image1)
    background_label1 = Label(root2, image=bg_image)
    background_label1.place(x=0, y=0, relwidth=1, relheight=1)

    label = tk.Label(root2, text='''Добро пожаловать в приложение "Умный Холодильник"!
    
    Здесь вы можете легко добавлять продукты, следить за их 
    сроком годности, получать уведомления о его истечении и 
    находить рецепты для приготовления вкусных блюд.

  Готовьте с удовольствием и без лишних забот!''', bg='#F6EFE4', fg="#C5A483", font=("Corbel bold", 25))
    label.pack(anchor=CENTER, pady=100)
    button = tk.Button(root2, text="Перейти в \n холодильник", fg="#B5977A", bg="#E8CAAC",
                       font=("Corbel bold", 20), command=root2.destroy)
    button.config(width=20, height=2)
    button.pack(anchor='center')


def show_image():
    global image_label
    image_label = tk.Label(root1)
    image_label.pack()
    image_label.config(image=image)
    root1.geometry("")
    root1.title("Умный Холодильник!")
    root1.after(2000, lambda: image_label.destroy())
    root1.after(2000, next_page)


root1 = tk.Tk()
root1.geometry("")
image = tk.PhotoImage(file="image-png.ppm")
show_image()

icon = ImageTk.PhotoImage(file='Subtract (1).png')
root1.iconphoto(False, icon)

root1.mainloop()

root = Tk()
root.title("Умный холодильник")
root.geometry('600x450+400+200')
root.wm_iconbitmap()

icon2 = ImageTk.PhotoImage(file='Subtract (1).png')
root.iconphoto(False, icon2)

root_bg = Image.open("fon.png")
bg_image = ImageTk.PhotoImage(root_bg)

background_label = Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label = Label(root, text='ХОЛОДИЛЬНИК', foreground="#B5977A", background="#F6EFE4", font=("Corbel bold", 15))
label.pack()

style = ttk.Style()
style.configure("Treeview", foreground="#AC9075", font=("Corbel bold", 12))

columns = ["Название продукта", "Срок годности", "Категория"]
table = ttk.Treeview(root, columns=columns, show="headings", style='Treeview')

for col in columns:
    table.heading(col, text=col)
table.pack()

example = [
    ("Морковь", "2024-03-26", "Овощи"),
    ("Молоко", "2024-03-24", "Молочные продукты"),
    ("Ватрушка", "2024-03-16", "Выпечка"),
    ("Яблоко", "2024-04-23", "Фрукты"),
    ("Курица", "2024-12-12", "Мясо и птица")
]


def check_expiration_date():
    now = datetime.datetime.now().date()
    for row in table.get_children():
        item = table.item(row)["values"]
        expiration_date = item[1]

        # Преобразовать строку в объект datetime.date
        expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()
        if expiration_date - now <= datetime.timedelta(days=0):
            messagebox.showwarning("Уведомление", f"Срок годности товара \"{item[0]}\" истек.")

        elif expiration_date - now <= datetime.timedelta(days=3):
            messagebox.showwarning("Уведомление", f"Срок годности товара \"{item[0]}\" подходит к концу.")


for i in example:
    table.insert("", "end", values=i)
selected_category = ""


def open_second_window():
    def add_to_table_with_category():
        l = Label(second_window, text="Введите данные:", fg="#AC9075", bg="#E8CAAC",
                  font=("Corbel bold", 15)).grid(row=90, column=0, columnspan=2)
        global selected_category
        new_data = tuple(data_entry.get() for data_entry in data_entries)
        table.insert("", "end", values=new_data + (selected_category,))
        second_window.withdraw()
        messagebox.showinfo("Успех", "Данные добавлены в таблицу")

    second_window = Toplevel()
    second_window.geometry('700x450+400+200')
    second_window.title("Категории")

    icon3 = ImageTk.PhotoImage(file='Subtract (1).png')
    second_window.iconphoto(False, icon3)

    background_label1 = Label(second_window, image=bg_image)
    background_label1.place(x=0, y=0, relwidth=1, relheight=1)

    def close():
        second_window.destroy()
    btn_close = Button(second_window, text='<-', fg="#AC9075", bg="#E8CAAC", font=("Corbel bold", 15), command=close)
    btn_close.grid(row=0, column=0)
    label_add_p = Label(second_window, text='Добавить продукт', font=("Corbel bold", 20),
                        fg="#AC9075", bg="#F6EFE4")
    label_add_p.grid(row=0, column=1)

    data_entries = []
    for i in range(len(columns) - 1):
        label = Label(second_window, text=f"{columns[i]}:", foreground="#AC9075", background="#F6EFE4",
                      font=("Corbel bold", 15))
        label.grid(row=i + 60, column=0)
        data_entry = Entry(second_window, fg="#AC9075", bg="#F6EFE4", width=30)
        data_entry.grid(row=i + 60, column=1)
        data_entries.append(data_entry)

    def select_category(category):
        global selected_category
        selected_category = category
        add_to_table_with_category()

    categories = ["Говядина", "Завтрак", "Курица", "Десерт", "Козлятина", "Баранина", "Разное",
                                        "Паста", "Свинина", "Морепродукты", "Гарнир", "Закуска", "Веганский",
                                        "Вегетарианский"]

    row_num = 1
    col_num = 0
    padx_val = 5
    pady_val = 5
    width_b = 13
    for category in categories:
        btn = Button(second_window, text=category, command=lambda cat=category: select_category(cat),
                        fg="#AC9075", bg="#E8CAAC", font=("Corbel bold", 15))
        btn.config(width=16, height=0)
        btn.grid(row=row_num, column=col_num, padx=padx_val, pady=pady_val, ipadx=width_b)
        col_num += 1
        if col_num == 3:
            col_num = 0
            row_num += 1


def open_recepies():
    os.system("python рецептертс+.py")


open_window_button = Button(root, text="Добавить продукт", command=open_second_window,
                                fg="#AC9075", bg="#E8CAAC", font=("Corbel bold", 12))
open_window_button.config(width=18, height=0)
open_window_button.place(x=310, y=380)

recepies_btn = Button(root, text='Рецепты', command=open_recepies, fg="#AC9075", bg="#E8CAAC",
                         font=("Corbel bold", 12))
recepies_btn.config(width=18, height=0)
recepies_btn.place(x=120, y=380)

check_button = tk.Button(root, text="Проверить срок годности", command=check_expiration_date, fg="#AC9075", bg="#E8CAAC",
                         font=("Corbel bold", 12))
check_button.config(width=23, height=0)
check_button.place(y=340, x=190)

root.mainloop()
