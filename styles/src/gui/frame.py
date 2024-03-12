import tkinter as tk
import customtkinter as ctk
from logic import functions
from logic import html
from logic import css
import tkinter.colorchooser as colorchooser


def run_gui():
    
    widgetlist=[]
    root = ctk.CTk()
    root.geometry("1920x1080")

    
    
    # Configure row weights
    for i in range(10):  # Adjusted to the number of rows needed
        root.grid_rowconfigure(i, weight=1)

    # Configure column weights
    root.grid_columnconfigure(0, weight=1, uniform="fixed")
    root.grid_columnconfigure(1, weight=3, uniform="fixed")
    root.grid_columnconfigure(2, weight=1, uniform="fixed")

    frame1 = ctk.CTkScrollableFrame(root, orientation="vertical", label_text="Layout")
    frame1.grid(row=0, column=0, rowspan=10, pady=10, padx=10, sticky="nsew")

    height = root.winfo_height()
    width = int(height * (16 / 9))

    frame2 = ctk.CTkScrollableFrame(root, width=width, height=height, fg_color='white', orientation="vertical")
    frame2.grid(row=2, column=1, rowspan=6, pady=10, padx=10, sticky="nsew")

    frame3 = ctk.CTkFrame(root)  # Removed label_text argument
    frame3.grid(row=1, column=2, columnspan=1, rowspan=10, pady=10, padx=10, sticky="nsew")
    tabview = ctk.CTkTabview(frame3)
    tabview.pack(padx=1, pady=1)

    tab_1 = tabview.add("tab 1")
    tabview.insert(0, "tab 2")
    tabview.add("tab 42")
    tabview.set("tab 42")
    tabview.delete("tab 42")
    tabview.insert(0, "tab 42")
    tabview.delete("tab 42")
    tabview.insert(1, "tab 42")
    tabview.delete("tab 42")

    tabview.move(0, "tab 2")

    frame4 = ctk.CTkFrame(root)
    frame4.grid(row=0, column=2, rowspan=1, pady=10, padx=10, sticky="nsew")

    for i in range(10):  # Adjusted to the number of rows needed
        frame2.grid_rowconfigure(i, weight=1)
        frame2.grid_columnconfigure(i, weight=1, uniform="fixed")

    frame5 = ctk.CTkScrollableFrame(root, orientation="vertical", label_text="Elements In Canvas")
    frame5.grid(row=7, column=0, rowspan=10, pady=10, padx=10, sticky="nsew")

    def add_button_to_frame2(frame2):
        new_button = ctk.CTkButton(frame2, text="New Button")
        new_button.grid()
        return new_button  

    def add_button_to_frame5(frame5):
        new_button = ctk.CTkButton(frame5, text="New Button")
        new_button.grid()
        return new_button  

    def add_button(frame2, frame5,widgetlist):
        widgetlist.append (add_button_to_frame2(frame2))
        button_frame5 = add_button_to_frame5(frame5)
        
        for widget in widgetlist:
            print(widget.cget("text"))
        
    button_add_button = ctk.CTkButton(frame1, text="Add Button", command=lambda:add_button(frame2, frame5,widgetlist))
    button_add_button.pack()

    
    
    """button_add_label = ctk.CTkButton(frame1, text="Add Label", command=lambda:add_label(frame2, frame5))
    button_add_label.pack()

    add_button_checkbox = ctk.CTkButton(frame1, text="Add CheckBox", command=lambda:add_checkbox(frame2, frame5))
    add_button_checkbox.pack()
    """
    button_f = ctk.CTkButton(frame4, text="Convert to HTML", command=lambda: (html.convert_frame2_details_to_html(frame2), css.convert_frame2_details_to_css(frame2)))
    button_f.pack()

    button_close = ctk.CTkButton(frame4, text="Close App", command=root.destroy)
    button_close.pack()

    property_frame = tabview.tab("tab 2")

    bg_canvas = tk.Canvas(property_frame, width=40, height=20, bg="white", highlightthickness=0)
    bg_canvas.grid(row=1, column=3, padx=(5, 0), sticky="w")

    fg_canvas = tk.Canvas(property_frame, width=40, height=20, bg="white", highlightthickness=0)
    fg_canvas.grid(row=2, column=3, padx=(5, 0), sticky="w")

    def open_color_picker_and_update_canvas(variable, canvas):
        color = colorchooser.askcolor()[1]
        if color:
            variable.set(color)
            canvas.configure(bg=color)

    # Entry and buttons for modifying properties
    text_var = tk.StringVar()
    bg_var = tk.StringVar()
    fg_var = tk.StringVar()
    
    
    


    property_frame.grid_columnconfigure(0, weight=1, uniform="fixed", pad=0)
    property_frame.grid_columnconfigure(1, weight=3, uniform="fixed", pad=0)
    property_frame.grid_columnconfigure(2, weight=1, uniform="fixed", pad=0)
    property_frame.grid_columnconfigure(3, weight=1, uniform="fixed", pad=0)

    ctk.CTkLabel(property_frame, text="Text:").grid(row=0, column=0, columnspan=2, sticky='w')
    text_entry = ctk.CTkEntry(property_frame, textvariable=text_var)
    text_entry.grid(row=0, column=0, columnspan=4, sticky="e")

    bg_button = ctk.CTkButton(property_frame, text="Background Color", command=lambda: open_color_picker_and_update_canvas(bg_var, bg_canvas))
    bg_button.grid(row=1, column=0, columnspan=3, sticky="w")

    fg_button = ctk.CTkButton(property_frame, text="Foreground Color", command=lambda: open_color_picker_and_update_canvas(fg_var, fg_canvas))
    fg_button.grid(row=2, column=0, columnspan=3, sticky="w")

    """
    button_delete = ctk.CTkButton(frame3, text="Delete Widget", command=delete_widget)
    button_delete.pack(side="left")  # Using pack instead of grid

    update_button = ctk.CTkButton(frame3, text="Update Properties", command=update_properties)
    update_button.pack(side="left") 
    """

    root.mainloop()

