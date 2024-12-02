import tkinter as tk
from tkinter import messagebox
import random
import webbrowser

whatsupp_number = "yore number"
pesan = "i want, now we are dating"

def pindah_button(button):
    new_x = random.randint(0, window.winfo_width() - button.winfo_width())
    new_y = random.randint(0, window.winfo_height() - button.winfo_height())