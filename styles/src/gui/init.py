import tkinter
import tkinter.ttk as ttk
import customtkinter

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.geometry("1000x500")
app.title("STYLES")


app.rowconfigure(0, weight=1)  
app.columnconfigure(0, weight=1)  
app.columnconfigure(1, weight=4)  
app.columnconfigure(2, weight=1)  


frame_lay = customtkinter.CTkScrollableFrame(app, orientation="vertical", label_text="Layout", corner_radius=0)
frame_lay.grid(row=0, column=0, rowspan=2, pady=10, padx=10, sticky="nsew")

frame_canv = tkinter.Frame(master=app)
frame_canv.grid(padx=20, pady=20, row=0, column=1, rowspan=3, sticky="nsew")

frame_inps = customtkinter.CTkScrollableFrame(app, orientation="vertical", label_text="Inspector", corner_radius=0)
frame_inps.grid(row=0, column=2, rowspan=2, pady=10, padx=10, sticky="nsew")



ttk_style = ttk.Style()
ttk_style.configure(frame_lay.winfo_class(), background='red')

app.mainloop()
