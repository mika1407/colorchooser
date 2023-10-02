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

def openFile():
   filepath = filedialog.askopenfilename(initialdir="c:\\Users\\konea\\Documents\\Python\\Test",
                                         title="Open file",
                                         filetypes=(("text files","*.txt"),
                                         ("all files","*.*")))
   file = open(filepath, 'r')
   print(file.read())
   file.close()

def cut():
   print("You cut some text!")
def copy():
   print("You copied some text!")
def paste():
   print("You pasted some text!")

window = Tk()

openImage = PhotoImage(file="files.png")
saveImage = PhotoImage(file="folder.png")

window.geometry("420x420")
menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",10))
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile,image=openImage,compound='left')
fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)

editMenu = Menu(menubar,tearoff=0,font=("MV Boli",10))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

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




