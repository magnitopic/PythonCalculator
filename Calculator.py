from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('200x200')
root.title("Calculator")
input = Entry(root, width=15)
input.grid(row=0, column=0, columnspan=3)
operators = list("+-/*")


def click(charecter):
    content = input.get()
    input.delete(0, END)
    input.insert(0, content + charecter)


def delete():
    position = len(input.get())-1
    input.delete(position, END)


def equal():
    firstNum, secondNum = 0, []
    content = list(input.get())
    print(content)
    for i in content:
        if i in operators:
            secondNum = float(''.join(secondNum))
            if i == "+":
                firstNum += secondNum
            elif i == "-":
                firstNum -= secondNum
            elif i == "÷":
                firstNum /= secondNum
            elif i == "×":
                firstNum *= secondNum
            secondNum = []
            input.delete(0, END)
            input.insert(0, firstNum)
        else:
            try:
                if i == ".":
                    i = ".0"
                secondNum.append(i)
                print("secondNUm:", secondNum)
            except:
                messagebox.showerror("ERROR", "Input is invalid. Try again.")
                break


delButton = Button(root, text="Del", command=delete)
delButton.grid(row=4, column=2)
equButton = Button(root, text="=", command=equal)
equButton.grid(row=4, column=3)
sumButton = Button(root, text="+", command=lambda: click("+"))
sumButton.grid(row=3, column=3)
subButton = Button(root, text="-", command=lambda: click("-"))
subButton.grid(row=2, column=3)
mulButton = Button(root, text="×", command=lambda: click("×"))
mulButton.grid(row=1, column=3)
divButton = Button(root, text="÷", command=lambda: click("÷"))
divButton.grid(row=0, column=3)
dotButton = Button(root, text=".", command=lambda: click("."))
dotButton.grid(row=4, column=1)
# Number buttons
zeroButton = Button(root, text="0", command=lambda: click("0"))
zeroButton.grid(row=4, column=0)
oneButton = Button(root, text="1", command=lambda: click("1"))
oneButton.grid(row=3, column=0)
twoButton = Button(root, text="2", command=lambda: click("2"))
twoButton.grid(row=3, column=1)
threeButton = Button(root, text="3", command=lambda: click("3"))
threeButton.grid(row=3, column=2)
fourButton = Button(root, text="4", command=lambda: click("4"))
fourButton.grid(row=2, column=0)
fiveButton = Button(root, text="5", command=lambda: click("5"))
fiveButton.grid(row=2, column=1)
sixButton = Button(root, text="6", command=lambda: click("6"))
sixButton.grid(row=2, column=2)
sevenButton = Button(root, text="7", command=lambda: click("7"))
sevenButton.grid(row=1, column=0)
eightButton = Button(root, text="8", command=lambda: click("8"))
eightButton.grid(row=1, column=1)
nineButton = Button(root, text="9", command=lambda: click("9"))
nineButton.grid(row=1, column=2)

root.mainloop()
