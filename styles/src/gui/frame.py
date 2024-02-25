from cProfile import label
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
    root.grid_columnconfigure(0, weight=1,uniform="fixed")
    root.grid_columnconfigure(1, weight=3,uniform="fixed")
    root.grid_columnconfigure(2, weight=1,uniform="fixed")

    frame1 = ctk.CTkScrollableFrame(root, orientation="vertical", label_text="Layout")
    frame1.grid(row=0, column=0, rowspan=10, pady=10, padx=10, sticky="nsew")

    height = root.winfo_height()
    width = int(height * (16 / 9))

    frame2 = ctk.CTkFrame(root, width=width, height=height, fg_color='white')
    frame2.grid(row=2, column=1, rowspan=6, pady=10, padx=10, sticky="nsew")


    frame3 = ctk.CTkScrollableFrame(root, orientation="vertical", label_text="Inspector")
    frame3.grid(row=1, column=2, columnspan=1, rowspan=10, pady=10, padx=10, sticky="nsew")

    frame4 = ctk.CTkFrame(root)
    frame4.grid(row=0, column=2, rowspan=1, pady=10, padx=10, sticky="nsew",)

    # Dictionary to keep track of the selected widget
    selection = {"widget": None}

    def select_widget(widget):
        print("Selecting widget:", widget)  # Print the widget being selected
        if selection["widget"]:
            print("Resetting previously selected widget appearance")
            selection["widget"].configure(relief=tk.FLAT)  # Reset previously selected widget appearance
        selection["widget"] = widget
        selection["widget"].configure(relief=tk.SUNKEN)  # Highlight currently selected widget
        print("Widget selection complete")


    button_add_button = ctk.CTkButton(frame1, text="Add Button", command=lambda: select_widget(functions.add_button_to_frame2(frame2)))
    button_add_button.pack()

    button_add_label = ctk.CTkButton(frame1, text="Add Label", command=lambda: select_widget(functions.add_label_to_frame2(frame2)))
    button_add_label.pack()

    add_button_checkbox = ctk.CTkButton(frame1, text="Add CheckBox", command=lambda: select_widget(functions.add_checkbox_to_frame2(frame2)))
    add_button_checkbox.pack()

    button_f = ctk.CTkButton(frame4, text="Convert to HTML", command=lambda: html.convert_frame2_details_to_html(frame2))
    button_f.pack()
    
    button_close=ctk.CTkButton(frame4,text="close app",command=root.destroy)
    button_close.pack()
    
    # Function to update properties from inspector panel
    def update_properties():
        selected_widget = selection["widget"]
        if selected_widget:
            # Update properties of the selected widget
            selected_widget.configure(**{
                "text": text_var.get(),
                "bg_color": bg_var.get(),
                "fg_color": fg_var.get(),
                "text_color": txtcol_var.get(),
                # Add more properties as needed
            })

    # Entry and buttons for modifying properties
    text_var = tk.StringVar()
    bg_var = tk.StringVar()
    fg_var = tk.StringVar()
    txtcol_var=tk.StringVar()
    
    property_frame = ctk.CTkFrame(frame3)
    property_frame.pack()

    ctk.CTkLabel(property_frame, text="Text:").pack()
    text_entry = ctk.CTkEntry(property_frame, textvariable=text_var)
    text_entry.pack()

    ctk.CTkLabel(property_frame, text="Background Color:").pack()
    bg_entry = ctk.CTkEntry(property_frame, textvariable=bg_var)
    bg_entry.pack()

    ctk.CTkLabel(property_frame, text="Foreground Color:").pack()
    fg_entry = ctk.CTkEntry(property_frame, textvariable=fg_var)
    fg_entry.pack()

    ctk.CTkLabel(property_frame, text="text color:").pack()
    fg_entry = ctk.CTkEntry(property_frame, textvariable=txtcol_var)
    fg_entry.pack()
    
    update_button = ctk.CTkButton(property_frame, text="Update Properties", command=update_properties)
    update_button.pack()

    root.mainloop()


