# functions.py
import tkinter as tk
import customtkinter as ctk

def add_button_to_frame2(frame2):
    new_button = ctk.CTkButton(frame2, text="New Button")
    new_button.grid()
    return new_button  


def add_label_to_frame2(frame2):
    new_label = ctk.CTkLabel(frame2, text="New Label",fg_color="blue")
    new_label.grid()
    return new_label

def add_checkbox_to_frame2(frame2):
    new_checkbox = ctk.CTkCheckBox(frame2,text ="Check Box",fg_color="blue")
    new_checkbox.grid()
    return new_checkbox

    # Dictionary to keep track of the selected widget
selection = {"widget": None}



    
