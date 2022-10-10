// Hudson Schumaker

import random 
from tkinter import *
from tkinter import messagebox

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'w', 'r', 's', 't', 'u', 'v', 'y', 'x', 'z']


def generate():
    global letters
    first = ""
    for x in range(5):
        first += letters[random.randint(0, 25)]

    first += str(random.randint(0, 9))

    second = ""
    for y in range(6):
        if y == 4:
            second += letters[random.randint(0, 25)].upper()
        else:
            second += letters[random.randint(0, 25)]

    third = ""
    for z in range(6):
        third += letters[random.randint(0, 25)]

    messagebox.showinfo(title="Password", message=first + "-" + second + "-" + third)


def create_window():
    _window = Tk()
    _window.title("Password")
    _window.geometry("200x150")
    _window.config(background="black")
    _button = Button(master=_window, text="generate", command=generate)
    _button.place(x=55, y=50)
    return _window


if __name__ == '__main__':
    window = create_window()
    window.mainloop()
