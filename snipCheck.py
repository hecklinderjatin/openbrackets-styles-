# website to add drag drop feature
#https://stackoverflow.com/questions/44887576/how-can-i-create-a-drag-and-drop-interface#:~:text=To%20use%20it%2C%20all%20you%20need%20to%20do,%3D%20Label%28canvas%2C%20image%3Dimage%29...%20dnd%20%3D%20DragManager%28%29%20dnd.add_dragable%28label%29...%20root.mainloop%28%29


import tkinter as tk

root = tk.Tk()
root.geometry("1920x1080")



  # Configure row weights
for i in range(10):
    root.grid_rowconfigure(i, weight=1)

# Configure column weights
root.grid_columnconfigure(0, weight=1, uniform="fixed")
root.grid_columnconfigure(1, weight=3, uniform="fixed")
root.grid_columnconfigure(2, weight=1, uniform="fixed")

buttons_list = []  # List to store buttons in frame2
delete_buttons_list = []
update_button_propertie =[]
    
labels_list = []
delete_labels_list = []
update_labels_propertie =[]


checkboxes_list = []
delete_checkboxes_list = []
update_checkboxes_propertie =[]


frame1 = tk.Frame(root, highlightthickness=1, highlightbackground="black")
frame1.grid(row=0, column=0, rowspan=10, pady=10, padx=10, sticky="nsew")

height = root.winfo_height()
width = int(height * (16 / 9))

frame2 = tk.Frame(root, width=width, height=height, bg='white', highlightthickness=1, highlightbackground="black")
frame2.grid(row=2, column=1, rowspan=6, pady=10, padx=10, sticky="nsew")

scrollbar_frame2 = tk.Scrollbar(frame2)
scrollbar_frame2.pack(side=tk.RIGHT, fill=tk.Y)

canvas_frame2 = tk.Canvas(frame2, bg='white', highlightthickness=0, yscrollcommand=scrollbar_frame2.set)
canvas_frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_frame2.config(command=canvas_frame2.xview)

frame2_inner = tk.Frame(canvas_frame2, bg='white')
canvas_frame2.create_window((10, 8), window=frame2_inner, anchor=tk.NW)

frame3 = tk.Frame(root, highlightthickness=1, highlightbackground="black")
frame3.grid(row=2, column=2, columnspan=1, rowspan=10, pady=10, padx=10, sticky="nsew")


frame4 = tk.Frame(root, highlightthickness=1, highlightbackground="black")
frame4.grid(row=0, column=2, rowspan=2, pady=10, padx=10, sticky="nsew")
for i in range(10):
        frame2.grid_rowconfigure(i, weight=1)
        frame2.grid_columnconfigure(i, weight=1, uniform="fixed")
    
frame5 = tk.Frame(root, highlightthickness=1, highlightbackground="black")
frame5.grid(row=7, column=0, rowspan=10, pady=10, padx=10, sticky="nsew")
def delete_buttons(button_index):
        buttons_list[button_index].destroy()
        delete_buttons_list[button_index].destroy()
        update_button_propertie[button_index].destroy()

        # Remove the deleted buttons from the lists
        del buttons_list[button_index]
        del delete_buttons_list[button_index]
        del update_button_propertie[button_index]

def delete_labels(label_index):
        labels_list[label_index].destroy()
        delete_labels_list[label_index].destroy()
        update_labels_propertie[label_index].destroy()

        # Remove the deleted label and its associated delete button from the lists
        del labels_list[label_index]
        del delete_labels_list[label_index]
        del update_labels_propertie[label_index]

def delete_checkboxes(checkbox_index):
        checkboxes_list[checkbox_index].destroy()
        delete_checkboxes_list[checkbox_index].destroy()
        update_checkboxes_propertie[checkbox_index].destroy()

        del checkboxes_list[checkbox_index]
        del delete_checkboxes_list[checkbox_index]
        del update_checkboxes_propertie[checkbox_index]



# def update_button_properties(button_index):
#         # Get the text from the text box
#         new_text = text_var.get()
#         # Update the text of the button
#         buttons_list[button_index].configure(text=new_text)
#         # Update background color
#         buttons_list[button_index].configure(bg=bg_var.get())
#         # Update foreground color
#         buttons_list[button_index].configure(fg=fg_var.get())

# def update_label_properties(label_index):
#         # Get the text from the text box
#         new_text = text_var.get()
#         # Update the text of the label
#         labels_list[label_index].configure(text=new_text)
#         # Update background color
#         labels_list[label_index].configure(bg=bg_var.get())
#         # Update foreground color
#         labels_list[label_index].configure(fg=fg_var.get())

# def update_checkbox_properties(checkbox_index):
#         # Get the text from the text box
#         new_text = text_var.get()
#         # Update the text of the checkbox
#         checkboxes_list[checkbox_index].configure(text=new_text)
#         # Update background color
#         checkboxes_list[checkbox_index].configure(bg=bg_var.get())
#         # Update foreground color
#         checkboxes_list[checkbox_index].configure(fg=fg_var.get())



def add_button():
        index = len(buttons_list) + 1
        new_button = tk.Button(frame2_inner, text=f"Dynamic Button {index}")
        new_button.pack()
        buttons_list.append(new_button)
        
        delete_button_button = tk.Button(frame5,text=f"Delete Button {index}", command=lambda index=index-1: delete_buttons(index))
        delete_button_button.grid(column=0)
        delete_buttons_list.append(delete_button_button)

        update_button_properties_button = tk.Button(frame5, text=f"Button Properties {index}", command=lambda index=index-1: update_button_properties(index))
        update_button_properties_button.grid(column=2)
        update_button_propertie.append(update_button_properties_button)  # Append the update button to the list


# def add_label():
#         index = len(labels_list) + 1
#         new_label = tk.Label(frame2_inner, text=f"Dynamic Label {index}")
#         new_label.pack()
#         labels_list.append(new_label)
        
#         delete_label_button = tk.Button(frame5, text=f"Delete Label {index}", command=lambda idx=index-1: delete_labels(idx))
#         delete_label_button.grid(column=0)
#         delete_labels_list.append(delete_label_button)

#         update_label_properties_button = tk.Button(frame5, text=f"Label Properties {index}", command=lambda index=index-1: update_label_properties(index))
#         update_label_properties_button.grid(column=2)
#         update_labels_propertie.append(update_label_properties_button)  # Append the update button to the list


# def add_checkbox():
#         index = len(checkboxes_list) + 1
#         new_checkbox = tk.Checkbutton(frame2_inner, text=f"Dynamic Checkbox {index}")
#         new_checkbox.pack()
#         checkboxes_list.append(new_checkbox)
        
#         delete_checkbox_button = tk.Button(frame5, text=f"Delete Checkbox {index}", command=lambda idx=index-1: delete_checkboxes(idx))
#         delete_checkbox_button.grid(column=0)
#         delete_checkboxes_list.append(delete_checkbox_button)

#         update_checkboxes_properties_button = tk.Button(frame5, text=f"Checkbox Properties {index}", command=lambda index=index-1: update_checkbox_properties(index))
#         update_checkboxes_properties_button.grid(column=2)
#         update_checkboxes_propertie.append(update_checkboxes_properties_button)  # Append the update button to the list

bg_canvas = tk.Canvas(frame3, width=40, height=20, bg="white", highlightthickness=0)
bg_canvas.grid(row=1, column=3, padx=(5, 0), sticky="w")

fg_canvas = tk.Canvas(frame3, width=40, height=20, bg="white", highlightthickness=0)
fg_canvas.grid(row=2, column=3, padx=(5, 0), sticky="w")

# def open_color_picker_and_update_canvas(variable, canvas):
#         color = colorchooser.askcolor()[1]
#         if color:
#             variable.set(color)
#             canvas.configure(bg=color)

    # Entry and buttons for modifying properties
text_var = tk.StringVar()
bg_var = tk.StringVar()
fg_var = tk.StringVar()

tk.Label(frame3, text="Text:").grid(row=0, column=0, columnspan=2, sticky='w')
text_entry = tk.Entry(frame3, textvariable=text_var)
text_entry.grid(row=0, column=0, columnspan=4, sticky="e")

bg_button = tk.Button(frame3, text="Background Color", command=lambda: open_color_picker_and_update_canvas(bg_var, bg_canvas))
bg_button.grid(row=1, column=0, columnspan=3, sticky="w")

fg_button = tk.Button(frame3, text="Foreground Color", command=lambda: open_color_picker_and_update_canvas(fg_var, fg_canvas))
fg_button.grid(row=2, column=0, columnspan=3, sticky="w")

tk.mainloop()