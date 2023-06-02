from tkinter import *
from pathlib import Path

import pyautogui
import os

window = Tk()
path_screen = Path('./tmp/screen.png')

window.title("OCR Translate Project")
window.geometry("900x300")

def checkExistingScreen():
   return path_screen.absolute().exists()

#debug options
def print_width():
   print("The width of Tkinter window:", window.winfo_width())
   print("The height of Tkinter window:", window.winfo_height())

def take_screenshot():
   if checkExistingScreen():
      screenTook = pyautogui.screenshot()
      screenTook.save(path_screen)

def popup_confirmation():
   top = Toplevel(window)
   top.geometry("400x200")
   top.title("Confirm")
   Label(top, text="Are you sure ?").place(x=160, y=80)

btn = Button(window, text="Screenshot", command=take_screenshot)
btn.place(x=80, y =200)


window.mainloop()