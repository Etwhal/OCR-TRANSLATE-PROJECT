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

def take_and_save():
      screenTook = pyautogui.screenshot()
      screenTook.save(path_screen)

def take_screenshot():
   if not checkExistingScreen():
      take_and_save()
   else:
      popup_confirmation()

def popup_confirmation():
   conf = Toplevel(window)
   conf.geometry("400x200")
   conf.title("Confirm")
   Label(conf, text="Are you sure ?").place(x=160, y=80)

   btn_overr = Button(conf, text="Override", command=override_screen).place(x=100, y=120)
   btn_add = Button(conf, text="Save + 1", command=add_screen).place(x=200, y=120)
   btn_cancel = Button(conf, text="Cancel", command=cancel_screen).place(x=300, y=120)

def override_screen():
   take_and_save()
def add_screen():
   print("add + 1")
def cancel_screen():
   print("cancel screen")

btn = Button(window, text="Screenshot", command=take_screenshot)
btn.place(x=80, y =200)


window.mainloop()