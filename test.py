from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog

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

def saveFile():
   file = filedialog.asksaveasfile(initialdir="C:\\Users\\konea\\Documents\\Python\\Test",
                                   defaultextension='.txt',
                                   filetypes=[
                                      ("Text file",".txt"),
                                      ("HTML file",".html"),
                                      ("All files", ".*"),
                                   ])
   if file is None:
      return
   filetext = str(text.get(1.0,END))
   #filetext = input("Enter some text please: ")
   file.write(filetext)
   file.close()

window = Tk()
window.geometry("420x420")
button = Button(text="change color",command=click)
button.pack()

text = Text(window,
            bg="light yellow",
            font=("Ink Free",14),
            height=12,
            width=32,
            padx=10,
            pady=10,
            fg="purple")
text.pack()
button = Button(window,text="submit",command=submit)
button.pack()

button = Button(text='save',command=saveFile)
button.pack()

window.mainloop()




