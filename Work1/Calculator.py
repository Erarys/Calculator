from tkinter import *
from tkinter import messagebox


def main_math():
    data["state"] = NORMAL
    try:
        res = eval(data.get())
        data.delete(0, END)
        data.insert(0, "{:.2f}".format(res))
        data["state"] = DISABLED
    except (NameError, ZeroDivisionError, SyntaxError) as info:
        messagebox.showinfo("Error", f"Код ошибки {info}")
        data.insert(0, "0")


def math(sign):
    data["state"] = NORMAL
    info = data.get()
    if info.endswith(("-", "+", "/", "*")):
        data.delete(0, END)
        data.insert(0, info[:-1])

    info_new = data.get()
    for i_elem in ("-", "+", "/", "*"):
        if i_elem in info_new:
            main_math()
            data["state"] = NORMAL
            info_new = data.get()

    data.delete(0, END)
    data.insert(0, info_new + sign)
    data["state"] = DISABLED


def abc():
    data["state"] = NORMAL
    info = data.get()
    if not info.endswith(("-", "+", "/", "*")):
        data.delete(0, END)
        data.insert(0, info + "*-1")
        main_math()
    data["state"] = DISABLED


def point():
    data["state"] = NORMAL
    info = data.get()
    if not info.endswith("."):
        data.delete(0, END)
        data.insert(0, info+".")
    data["state"] = DISABLED


def delete():
    data["state"] = NORMAL
    data.delete(len(data.get()) - 1)
    if len(data.get()) == 0:
        data.insert(0, "0")
    data["state"] = DISABLED


def clear():
    data["state"] = NORMAL
    data.delete(0, END)
    data.insert(0, "0")
    data["state"] = DISABLED


def add_num(num):
    data["state"] = NORMAL
    info = data.get()
    if info.startswith("0"):
        data.delete(0)
    if len(info) < 16:
        info = data.get() + num
        data.delete(0, END)
        data.insert(0, info)
    data["state"] = DISABLED


def create_math_button(sign, r, c):
    return Button(
        text=sign,
        fg="White",
        bg="#323232",
        font=("Arial", 20, "italic"),
        activebackground="#323232",
        activeforeground="#DCDCDC",
        command=lambda: math(sign)
    ). \
        grid(
        row=r,
        column=c,
        padx=1,
        pady=1,
        sticky="wens"
    )


def create_button(num, r, c):
    return Button(
        text=num,
        font=("Arial", 20, "italic"),
        bg="#3B3B3B",
        fg="White",
        activebackground="#323232",
        activeforeground="#DCDCDC",
        command=lambda: add_num(num)
    ). \
        grid(
        row=r,
        column=c,
        padx=1,
        pady=1,
        sticky="wens"
    )


def keyword(res):
    print(repr(res.char))
    if res.char.isdigit():
        add_num(res.char)
    elif res.char in "-+/*":
        add_num(res.char)
    elif res.char == "\r":
        main_math()
    elif res.char == ".":
        point()


root = Tk()
# Setting
root.title("Калькулятор")
root.geometry("500x350")
icon = PhotoImage(file="icon.png")
root.iconphoto(False, icon)
root.config(bg="#202020")
# Keyword
root.bind("<Key>", keyword)

# Entry
data = Entry(bg="#202020", fg="White", justify=RIGHT, font=("Arial", 30))
data.grid(columnspan=4, pady=5, sticky="wens")
data.insert(0, "0")
data["state"] = DISABLED
# Button
create_button("7", r=2, c=0)
create_button("8", r=2, c=1)
create_button("9", r=2, c=2)
create_button("4", r=3, c=0)
create_button("5", r=3, c=1)
create_button("6", r=3, c=2)
create_button("1", r=4, c=0)
create_button("2", r=4, c=1)
create_button("3", r=4, c=2)
create_button("0", r=5, c=1)

# Delete
Button(
    text="C",
    font=("Arial", 15, "italic"),
    bg="#323232",
    fg="White",
    activebackground="#323232",
    activeforeground="#DCDCDC",
    command=clear
). \
    grid(
    row=1,
    column=1,
    sticky="wens",
    padx=1,
    pady=1
)

# Delete one
Button(
    text="⌫",
    font=("Arial", 15),
    bg="#323232",
    fg="white",
    activebackground="#323232",
    activeforeground="#DCDCDC",
    command=delete
). \
    grid(
    row=1,
    column=2,
    padx=1,
    pady=1,
    sticky="wens"
)
# Math Elem
create_math_button("/", 1, 3)
create_math_button("*", 2, 3)
create_math_button("-", 3, 3)
create_math_button("+", 4, 3)


# Result
Button(
    text="=",
    font=("Arial", 20, "italic"),
    bg="#A6F7D0",
    fg="#395548",
    activebackground="#8ACBAC",
    activeforeground="#5E8B75",
    command=main_math
). \
    grid(
    row=5,
    column=3,
    sticky="wens",
    padx=1,
    pady=1
)
# Point
Button(
    text="○",
    font=("Arial", 25, "italic"),
    bg="#3B3B3B",
    fg="White",
    activebackground="#323232",
    activeforeground="#DCDCDC",
    command=point
). \
    grid(
    row=5,
    column=2,
    sticky="wens",
    padx=1,
    pady=1
)
# ABS
Button(
    text="+/-",
    font=("Arial", 25, "italic"),
    bg="#3B3B3B",
    fg="White",
    activebackground="#323232",
    activeforeground="#DCDCDC",
    command=abc
). \
    grid(
    row=5,
    column=0,
    sticky="wens",
    padx=1,
    pady=1
)

# Row
root.grid_columnconfigure(0, minsize=125)
root.grid_columnconfigure(1, minsize=125)
root.grid_columnconfigure(2, minsize=125)
root.grid_columnconfigure(3, minsize=125)
# Col
root.grid_rowconfigure(0, minsize=58)
root.grid_rowconfigure(1, minsize=58)
root.grid_rowconfigure(2, minsize=58)
root.grid_rowconfigure(3, minsize=58)
root.grid_rowconfigure(4, minsize=58)
root.grid_rowconfigure(5, minsize=58)

root.mainloop()
