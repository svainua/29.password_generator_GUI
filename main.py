from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]     # in range в данном случае говорит, сколько раз должно произойти действие
password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

password_list = password_letters + password_symbols + password_numbers
random.shuffle(password_list)                                               # перемешивает элементы списка


def create_password():
    password = "".join(password_list)               # функция join объединяет элементы.
    entry_password.insert(0, password)
    pyperclip.copy(password)                # копирует то, что получается после нажатия кнопки. можно потом вставлять в документ

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = entry_website.get()                   # получаем инфу из полей для ввода
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Not all the data were provided")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                          f"\nPassword: {password} \nIs it OK to save?")  # вызываем окно, чтобы спросить польхователя о дальнейших действиях
        if is_ok:
            with open("data.txt", mode="a") as data:                    # создаем текстовый файл в режиме append и далее вносим в него информацию
                data.write(f"{website} | {email} | {password}\n")
            entry_website.delete(0, END)                                # удаляем из полей инфу, чтобы можно было снова пользоваться программой
            entry_email.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

#Labels
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
label_email_username = Label(text="Email/Username:")
label_email_username.grid(row=2, column=0)
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

#Entries
entry_website = Entry(width=35)
entry_website.grid(row=1, column=1, columnspan=2, sticky="w")
entry_website.focus()
entry_email = Entry(width=35)
entry_email.insert(0, "rollik2005@ya.ru")
entry_email.grid(row=2, column=1, columnspan=2, sticky="w")
entry_password = Entry(width=21)
entry_password.grid(row=3, column=1, sticky="w")

#Buttons
button_generate_password = Button(text="Generate Password", command=create_password)
button_generate_password.grid(row=3, column=2, sticky="w")
button_add = Button(text="Add", width=35, command=save)
button_add.grid(row=4, column=1, columnspan=2, sticky="w")


window.mainloop()