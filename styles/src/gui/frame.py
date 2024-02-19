import tkinter as tk
import tkinter.ttk as ttk
import customtkinter
from logic.functions import *


def run_tkinter_app():
    customtkinter.set_appearance_mode("dark")

    app = customtkinter.CTk()
    app.geometry("1000x500")
    app.title("STYLES")

    app.grid_rowconfigure(1, weight=1)
    app.grid_rowconfigure(0, weight=1)
    app.grid_rowconfigure(1, weight=4)
    app.grid_rowconfigure(2, weight=1)

    root = customtkinter.CTk()

    frame_lay = customtkinter.CTkScrollableFrame(root, orientation="vertical", label_text="Layout", corner_radius=0)
    frame_lay.grid(row=0, column=0, rowspan=2, pady=10, padx=10, sticky="nsew")
    add_button_button = customtkinter.CTkButton(frame_lay, text="Add Button", command=add_button)
    add_button_button.pack()

    add_label_button = customtkinter.CTkButton(frame_lay, text="Add Label", command=add_label)
    add_label_button.pack()

    global frame_canv  # Define frame_canv as global
    frame_canv = customtkinter.CTkFrame(root)
    frame_canv.grid(padx=10, pady=10, row=0, column=1, rowspan=4, sticky="nsew")

    frame_inps = customtkinter.CTkScrollableFrame(root, orientation="vertical", label_text="Inspector", corner_radius=0)
    frame_inps.grid(row=0, column=2, rowspan=2, pady=10, padx=10, sticky="nsew")

    frame_save = customtkinter.CTkFrame(root)
    frame_save.grid(padx=20, pady=20, row=0, column=3, sticky="nsew")
    label_save = customtkinter.CTkLabel(master=frame_save, text="EXPORT", fg_color=("gray95", "gray15"))
    label_save.grid(row=0, column=0, columnspan=1, padx=5, pady=5, sticky="ew")
    button_save = customtkinter.CTkButton(frame_save, text="SAVE", command=convert_to_html)
    button_save.grid(row=1, column=0, padx=20)
    frame_save.grid_rowconfigure(1, weight=1)
    frame_save.grid_columnconfigure((0,), weight=1)

    ttk_style = ttk.Style()
    ttk_style.configure(frame_lay.winfo_class(), background='red')

    app.mainloop()


def add_button():
    new_button = customtkinter.CTkButton(frame_canv, text="New Button")
    new_button.pack()


def add_label():
    new_label = customtkinter.CTkLabel(frame_canv, text="New Label")
    new_label.pack()


def convert_to_html():
    details = ""
    children = frame_canv.winfo_children()
    for child in children:
        if isinstance(child, customtkinter.CTkButton) or isinstance(child, customtkinter.CTkLabel):
            details += f"{child['text']}<br>"

    # Save details to an HTML file
    with open("output.html", "w") as html_file:
        html_file.write("<html><body>")
        html_file.write(details)
        html_file.write("</body></html>")


run_tkinter_app()  # Call the function to start the application
