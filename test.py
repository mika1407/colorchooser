from tkinter import *
from tkinter import colorchooser

def click():
  # color = colorchooser.askcolor()
  # print(color)
  # colorHex = color[1]
  # print(colorHex)
  # window.config(bg=colorHex)
  window.config(bg=colorchooser.askcolor()[1])

def submit():
    input = text.get("1.0",END)
    print(input)

window = Tk()
window.geometry("420x420")
button = Button(text="change color",command=click)
button.pack()

text = Text(window,
            bg="light yellow",
            font=("Ink Free",14),
            height=14,
            width=32,
            padx=10,
            pady=10,
            fg="purple")
text.pack()
button = Button(window,text="submit",command=submit)
button.pack()

window.mainloop()




