# frame.py

import tkinter as tk
import customtkinter as ctk
from logic import functions
from logic import html  # Correct import statement

def run_gui():
    root = ctk.CTk()

    frame1 = ctk.CTkFrame(root)
    frame1.pack(side=tk.LEFT)

    frame2 = ctk.CTkFrame(root)
    frame2.pack(side=tk.LEFT)

    button_add_button = ctk.CTkButton(frame1, text="Add Button", command=lambda: functions.add_button_to_frame2(frame2))
    button_add_button.pack()

    button_add_label = ctk.CTkButton(frame1, text="Add Label", command=lambda: functions.add_label_to_frame2(frame2))
    button_add_label.pack()

    button_f = ctk.CTkButton(root, text="Convert to HTML", command=lambda: html.convert_frame2_details_to_html(frame2))  # Correct function call
    button_f.pack()

    root.mainloop()

if __name__ == "__main__":
    run_gui()
