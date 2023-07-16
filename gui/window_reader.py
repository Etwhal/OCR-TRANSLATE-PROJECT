from tkinter import *
from pathlib import Path

import pyautogui
import os

window = Tk()
path_screen = Path('./tmp/screen.png')

window.title("OCR Translate Project")
window.geometry("400x250")

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

def override_screen():
   take_and_save()

def add_screen():
   # path_screen = path_screen.absolute(). 
   return
   
def cancel_screen(w):
   w.destroy()

def popup_confirmation():
   conf = Toplevel(window)
   conf.geometry("400x200")
   conf.title("Confirm")
   Label(conf, text="Are you sure ?").place(x=160, y=80)

   btn_overr = Button(conf, text="Override", command=override_screen).place(x=100, y=120)
   btn_add = Button(conf, text="Save + 1", command=add_screen).place(x=200, y=120)
   btn_cancel = Button(conf, text="Cancel", command=lambda: cancel_screen(conf)).place(x=300, y=120)

btn = Button(window, text="Screenshot", command=take_screenshot)
btn.place(x=80, y =200)

Label(window, text="Welcome to the OCR Translation Project").place(x=75, y=50)

if checkExistingScreen():
   Label(window, text="A screen already exist !").place(x=75, y=80)

window.mainloop()