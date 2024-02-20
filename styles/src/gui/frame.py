# frame.py
import tkinter as tk
import customtkinter as ctk
from logic import functions
from logic import html 


def run_gui():

    root = ctk.CTk()
    root.geometry("1920x1080")
    
    # Configure row weights
    for i in range(10):  # Adjusted to the number of rows needed
        root.grid_rowconfigure(i, weight=1)

    # Configure column weights
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)
    root.grid_columnconfigure(2, weight=1)

    

    frame1 = ctk.CTkScrollableFrame(root, orientation="vertical", label_text="Layout")
    frame1.grid(row=0, column=0, rowspan=10, pady=10, padx=10, sticky="nsew")

    height = root.winfo_height()
    width = int(height * (16 / 9))

    frame2 = ctk.CTkFrame(root, width=width, height=height)
    frame2.place(x=960, y=540)

    frame3 = ctk.CTkScrollableFrame(root, orientation="vertical", label_text="Inspector")
    frame3.grid(row=1, column=2, columnspan=1, rowspan=10, pady=10, padx=10, sticky="nsew")

    frame4 = ctk.CTkFrame(root)
    frame4.grid(row=0, column=2, rowspan=1, pady=10, padx=10, sticky="nsew")

    button_add_button = ctk.CTkButton(frame1, text="Add Button", command=lambda: functions.add_button_to_frame2(frame2))
    button_add_button.pack()

    button_add_label = ctk.CTkButton(frame1, text="Add Label", command=lambda: functions.add_label_to_frame2(frame2))
    button_add_label.pack()

    add_button_checkbox = ctk.CTkButton(frame1, text="Add CheckBox", command=lambda: functions.add_checkbox_to_frame2(frame2))
    add_button_checkbox.pack()

    button_f = ctk.CTkButton(frame4, text="Convert to HTML", command=lambda: html.convert_frame2_details_to_html(frame2))
    button_f.pack()

    root.mainloop()

if __name__ == "__main__":
    run_gui()
