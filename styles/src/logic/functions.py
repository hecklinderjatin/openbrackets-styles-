import tkinter as tk
import customtkinter as ctk


def add_button_to_frame2(frame2):
    new_button = ctk.CTkButton(frame2, text="New Button")
    new_button.grid()
    return new_button  

def add_button_to_frame5(frame5):
    new_button = ctk.CTkButton(frame5, text="New Button")
    new_button.grid()
    return new_button  

def add_button(frame2, frame5):
    button_frame2 = add_button_to_frame2(frame2)
    button_frame5 = add_button_to_frame5(frame5)
    return button_frame2, button_frame5

def add_label_to_frame2(frame2):
    new_label = ctk.CTkLabel(frame2, text="New Label", fg_color="blue")
    new_label.grid()
    return new_label

def add_label_to_frame5(frame5):
    new_label = ctk.CTkButton(frame5, text="New Label")
    new_label.grid()
    return new_label  

def add_label(frame2, frame5):
    label_frame2 = add_label_to_frame2(frame2)
    label_frame5 = add_label_to_frame5(frame5)
    return label_frame2, label_frame5

def add_checkbox_to_frame2(frame2):
    new_checkbox = ctk.CTkCheckBox(frame2, text="Check Box", fg_color="blue")
    new_checkbox.grid()
    return new_checkbox

def add_checkbox_to_frame5(frame5):
    new_checkbox = ctk.CTkButton(frame5, text="Check Box")
    new_checkbox.grid()
    return new_checkbox  

def add_checkbox(frame2, frame5):
    checkbox_frame2 = add_checkbox_to_frame2(frame2)
    checkbox_frame5 = add_checkbox_to_frame5(frame5)
    return checkbox_frame2, checkbox_frame5
