import tkinter
import tkinter.ttk as ttk
import customtkinter
from logic.functions import *


def add_button(frame):
    new_button = customtkinter.CTkButton(frame, text="New Button")
    new_button.pack()


def run_tkinter_app():
    customtkinter.set_appearance_mode("dark")

    app = customtkinter.CTk()
    app.geometry("1000x500")
    app.title("STYLES")

    app.grid_rowconfigure(1, weight=1)
    app.grid_rowconfigure(0, weight=1)
    app.grid_rowconfigure(1, weight=4)
    app.grid_rowconfigure(2, weight=1)

    frame_lay = customtkinter.CTkScrollableFrame(app, orientation="vertical", label_text="Layout", corner_radius=0)
    frame_lay.grid(row=0, column=0, rowspan=2, pady=10, padx=10, sticky="nsew")    
    add_button_button = customtkinter.CTkButton(frame_lay, text="Add Button", command=lambda: add_button(frame_canv))
    add_button_button.pack()

    frame_canv = customtkinter.CTkFrame(master=app)
    frame_canv.grid(padx=10, pady=10, row=0, column=1, rowspan=4, sticky="nsew")

    frame_inps = customtkinter.CTkScrollableFrame(app, orientation="vertical", label_text="Inspector", corner_radius=0)
    frame_inps.grid(row=0, column=2, rowspan=2, pady=10, padx=10, sticky="nsew")

    ttk_style = ttk.Style()
    ttk_style.configure(frame_lay.winfo_class(), background='red')

    app.mainloop()



