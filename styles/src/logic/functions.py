import tkinter as tk
import customtkinter as ctk
from gui import frame

widgetlist = []

def add_button_to_frame2(frame2):
    new_button = ctk.CTkButton(frame2, text="New Button")
    new_button.grid()
    return new_button  

def add_button_to_frame5(frame5):
    new_button = ctk.CTkButton(frame5, text="New Button")
    new_button.grid()
    return new_button  

def add_button(frame2, frame5, widgetlist):
    widgetlist.append(add_button_to_frame2(frame2))
    button_frame5 = add_button_to_frame5(frame5)

def add_label_to_frame2(frame2):
    new_label = ctk.CTkLabel(frame2, text="New Label", fg_color="blue")
    new_label.grid()
    return new_label

def add_label_to_frame5(frame5):
    new_label = ctk.CTkLabel(frame5, text="New Label")
    new_label.grid()
    return new_label  

def add_label(frame2, frame5, widgetlist):
    widgetlist.append(add_label_to_frame2(frame2))
    label_frame5 = add_label_to_frame5(frame5)

def add_checkbox_to_frame2(frame2):
    new_checkbox = ctk.CTkCheckBox(frame2, text="Check Box", fg_color="blue")
    new_checkbox.grid()
    return new_checkbox

def add_checkbox_to_frame5(frame5):
    new_checkbox = ctk.CTkCheckBox(frame5, text="Check Box")
    new_checkbox.grid()
    return new_checkbox  

def add_checkbox(frame2, frame5 , widgetlist):
    widgetlist.append(add_checkbox_to_frame2(frame2))
    checkbox_frame5 = add_checkbox_to_frame5(frame5)

def set_focus_to_widget(event, frame):
    # Iterate through the buttons in frame
    for index, widget in enumerate(frame.winfo_children()):
        # Check if the clicked widget is a button in frame
        if isinstance(widget, ctk.CTkButton) and widget == event.widget:
            print("Clicked button index:", index)
            break

def delete_selected_widget(root, frame5, selected_widget):
    # Get the currently selected widget (if any)
    selected_widget = root.focus_get()

    # Check if a widget is selected and if it belongs to frame5
    if selected_widget and selected_widget.master == frame5:
        print("Deleting Widget:", selected_widget)
        # Remove the widget from widgetlist and destroy it
        if selected_widget in widgetlist:
            widgetlist.remove(selected_widget)
            selected_widget.destroy()
    else:
        print("No widget selected or widget doesn't belong to frame5")
