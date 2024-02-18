import tkinter
import tkinter.ttk as ttk
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("STYLES")
        self.geometry("1000x500")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)


app = App()
app.mainloop()
