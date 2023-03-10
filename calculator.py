from tkinter import *

root = Tk()
root.title("My Calculator")

e = Entry(root, width=45, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def myClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + number)


def clear():
    e.delete(0, END)


def add_Button():
    first_number = e.get()
    e.delete(0, END)
    global f_num
    f_num = int(first_number)


def equal_Button():
    se_num = e.get()
    e.delete(0, END)
    s_num = int(se_num)
    e.insert(0, int(f_num) + int(s_num))


button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: myClick("1"))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: myClick("2"))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: myClick("3"))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: myClick("4"))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: myClick("5"))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: myClick("6"))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: myClick("7"))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: myClick("8"))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: myClick("9"))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: myClick("0"))
button_add = Button(root, text='+', padx=39, pady=20, command=add_Button)
button_clear = Button(root, text='clear', padx=79, pady=20, command=clear)
button_equal = Button(root, text='=', padx=91, pady=20, command=equal_Button)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0, )
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()
