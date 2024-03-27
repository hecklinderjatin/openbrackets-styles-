import tkinter as tk
from tkinter import ttk

widgetlist = []

def add_button_to_frame2(frame2):
    new_button = ttk.Button(frame2, text="New Button")
    new_button.grid()
    return new_button  

def add_button_to_frame5(frame5):
    new_button = ttk.Button(frame5, text="New Button")
    new_button.grid()
    return new_button  

def add_button(frame2, frame5, widgetlist):
    widgetlist.append(add_button_to_frame2(frame2))
    button_frame5 = add_button_to_frame5(frame5)

def add_label_to_frame2(frame2):
    new_label = ttk.Label(frame2, text="New Label", foreground="blue")
    new_label.grid()
    return new_label

def add_label_to_frame5(frame5):
    new_label = ttk.Label(frame5, text="New Label")
    new_label.grid()
    return new_label  

def add_label(frame2, frame5, widgetlist):
    widgetlist.append(add_label_to_frame2(frame2))
    label_frame5 = add_label_to_frame5(frame5)

def add_checkbox_to_frame2(frame2):
    new_checkbox = ttk.Checkbutton(frame2, text="Check Box",)
    new_checkbox.grid()
    return new_checkbox

def add_checkbox_to_frame5(frame5):
    new_checkbox = ttk.Checkbutton(frame5, text="Check Box")
    new_checkbox.grid()
    return new_checkbox  

def add_checkbox(frame2, frame5 , widgetlist):
    widgetlist.append(add_checkbox_to_frame2(frame2))
    checkbox_frame5 = add_checkbox_to_frame5(frame5)