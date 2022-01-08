from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('500x400')
root.title("Calculator")
input = Entry(root, width=35)
input.grid(row=0, column=0, padx="10", pady="10", columnspan=3)
operators = list("+-÷×")


def click(charecter):
    input.insert(END, charecter)


def delete():
    position = len(input.get())-1
    input.delete(position, END)


def equal():
    content = input.get()
    try:
        content=eval(content)
    except:
        messagebox.showerror("ERROR", "Input is invalid. Try again.")
        input.delete(0, END)
    else:
        input.delete(0, END)
        input.insert(0, content)


delButton = Button(root, text="Del", padx="40", pady="20", command=delete)
delButton.grid(row=4, column=2)
equButton = Button(root, text="=", padx="40", pady="20", command=equal)
equButton.grid(row=4, column=3)
sumButton = Button(root, text="+", padx="40", pady="20",
                   command=lambda: click("+"))
sumButton.grid(row=3, column=3)
subButton = Button(root, text="-", padx="40", pady="20",
                   command=lambda: click("-"))
subButton.grid(row=2, column=3)
mulButton = Button(root, text="×", padx="40", pady="20",
                   command=lambda: click("×"))
mulButton.grid(row=1, column=3)
divButton = Button(root, text="÷", padx="40", pady="20",
                   command=lambda: click("÷"))
divButton.grid(row=0, column=3)
dotButton = Button(root, text=".", padx="40", pady="20",
                   command=lambda: click("."))
dotButton.grid(row=4, column=1)
# Number buttons
zeroButton = Button(root, text="0", padx="40", pady="20",
                    command=lambda: click("0"))
zeroButton.grid(row=4, column=0)
oneButton = Button(root, text="1", padx="40", pady="20",
                   command=lambda: click("1"))
oneButton.grid(row=3, column=0)
twoButton = Button(root, text="2", padx="40", pady="20",
                   command=lambda: click("2"))
twoButton.grid(row=3, column=1)
threeButton = Button(root, text="3", padx="40", pady="20",
                     command=lambda: click("3"))
threeButton.grid(row=3, column=2)
fourButton = Button(root, text="4", padx="40", pady="20",
                    command=lambda: click("4"))
fourButton.grid(row=2, column=0)
fiveButton = Button(root, text="5", padx="40", pady="20",
                    command=lambda: click("5"))
fiveButton.grid(row=2, column=1)
sixButton = Button(root, text="6", padx="40", pady="20",
                   command=lambda: click("6"))
sixButton.grid(row=2, column=2)
sevenButton = Button(root, text="7", padx="40", pady="20",
                     command=lambda: click("7"))
sevenButton.grid(row=1, column=0)
eightButton = Button(root, text="8", padx="40", pady="20",
                     command=lambda: click("8"))
eightButton.grid(row=1, column=1)
nineButton = Button(root, text="9", padx="40", pady="20",
                    command=lambda: click("9"))
nineButton.grid(row=1, column=2)

root.mainloop()
