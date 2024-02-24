# functions.py
import tkinter as tk
import customtkinter as ctk

def add_button_to_frame2(frame2):
    new_button = ctk.CTkButton(frame2, text="New Button")
    new_button.pack()

def add_label_to_frame2(frame2):
    new_label = ctk.CTkLabel(frame2, text="New Label",fg_color="blue")
    new_label.pack()
    pass

def add_checkbox_to_frame2(frame2):
    new_checkbox = ctk.CTkCheckBox(frame2,text="Check Box",fg_color="blue")
    new_checkbox.pack()
    pass