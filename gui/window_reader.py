from tkinter import *

window = Tk()

window.title("OCR Translate Project")
# Geometry is height x width (why ??????? why not the other way around ??????
# (nvm its always like this im dumb))
window.geometry("900x300")

def print_width():
   print("The width of Tkinter window:", window.winfo_width())
   print("The height of Tkinter window:", window.winfo_height())

btn = Button(window, text="Click", command=print_width)
btn.place(x=80, y =200)


window.mainloop()