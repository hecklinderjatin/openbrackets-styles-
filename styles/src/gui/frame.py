import tkinter as tk
from tkinter import colorchooser
from tkinter import ttk
from tkinter import font
from logic import html
from logic import css
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import shutil

saved_image_path = ""
saved_image_path2 = ""
#hello

def run_gui():

    buttons_list = []  # List to store buttons in frame2
    delete_buttons_list = []
    update_button_propertie =[]
    
    labels_list = []
    delete_labels_list = []
    update_labels_propertie =[]

    checkboxes_list = []
    delete_checkboxes_list = []
    update_checkboxes_propertie =[]

    image_list=[]
    delete_image_list=[]
    update_image_list=[]

    root = tk.Tk()
    root.geometry("1920x1080")
    root.title("Styles : Web Builder")

    

    # Configure row weights
    for i in range(10):
        root.grid_rowconfigure(i, weight=1)

    # Configure column weights
    root.grid_columnconfigure(0, weight=1, uniform="fixed")
    root.grid_columnconfigure(1, weight=3, uniform="fixed")
    root.grid_columnconfigure(2, weight=1, uniform="fixed")

    def on_drag_start(event):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y

    def on_drag_motion(event):
        widget = event.widget
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y

        # Limit the movement to within the boundaries of frame2
        max_x = frame2_inner.winfo_width() - widget.winfo_width()
        max_y = frame2_inner.winfo_height() - widget.winfo_height()
        x = min(max(x, 0), max_x)
        y = min(max(y, 0), max_y)

        widget.place(x=x, y=y)

        inyx_var.set(str(x))
        inyy_var.set(str(y))

        # Calculate percentage position
        frame_width = frame2_inner.winfo_width()
        frame_height = frame2_inner.winfo_height()
        percentage_x = (x / frame_width) * 100
        percentage_y = (y / frame_height) * 100

        # Update text box with percentage values
        inyx_var.set(f"{percentage_x:.2f}%")
        inyy_var.set(f"{percentage_y:.2f}%")


    def on_drag_end(event):
        pass

    file_path = ""  # Define file_path as a global variable outside any function
    file_path1 = ""  # Define file_path as a global variable outside any function


    def open_image():
        global file_path  # Use the global keyword to access the global file_path variable
        file_path = filedialog.askopenfilename()
        if file_path:
            # Display the image
            display_image(file_path)
            # Save the image to the file folder
            save_image(file_path)

    def save_image(file_path):
        global saved_image_path
        directory = "E:\\openbrackets-styles-\\"
        os.makedirs(directory, exist_ok=True)
        file_name = os.path.basename(file_path)
        destination = os.path.join(directory, file_name)
        try:
            shutil.copyfile(file_path, destination)
            # Update the global variable with the saved image path
            saved_image_path = file_name
            destination.replace("\\", "/")  # Print the file path in the desired format
            return destination  # Return the destination path
        except Exception as e:
            print("Error saving the image:", e)
            return ""  # Return an empty string if there's an error

        
    def display_image(file_path):
        nonlocal picbox
        try:
            # Open the image file
            image = Image.open(file_path)
            # Resize the image to fit the dimensions of picbox
            width, height = picbox.winfo_width(), picbox.winfo_height()
            image = image.resize((width, height), Image.LANCZOS)
            # Convert the resized image to PhotoImage
            photo = ImageTk.PhotoImage(image)
            # Update the picbox with the resized image
            picbox.config(image=photo)
            picbox.image = photo  # Keep a reference to avoid garbage collection
        except Exception as e:
            print("Error opening or displaying image:", e)

    frame1 = tk.Frame(root, highlightthickness=1, highlightbackground="black")
    frame1.grid(row=0, column=0, rowspan=10, pady=10, padx=10, sticky="nsew")

    scrollbar_frame1 = tk.Scrollbar(frame1)
    scrollbar_frame1.pack(side=tk.RIGHT, fill=tk.Y)

    height = 720
    width = int(height * (16 / 9))

    frame2 = tk.Frame(root, width=width, height=height, bg='white', highlightthickness=1, highlightbackground="black")
    frame2.grid(row=2, column=1,rowspan=6, pady=10, padx=10, sticky="nsew")

    # Adding scrollbar to frame2
    scrollbar_frame2 = tk.Scrollbar(frame2)
    scrollbar_frame2.pack(side=tk.RIGHT, fill=tk.Y)

    canvas_frame2 = tk.Canvas(frame2, bg='white', highlightthickness=0, yscrollcommand=scrollbar_frame2.set)
    canvas_frame2.pack(fill=tk.BOTH, expand=True)

    scrollbar_frame2.config(command=canvas_frame2.yview)

    frame2_inner = tk.Frame(canvas_frame2, bg='white')
    canvas_frame2.create_window((0, 0), window=frame2_inner, anchor=tk.NW)

    # Create a label widget to display the image
    image_label = tk.Label(frame2_inner,width=width, height =height)
    image_label.pack()


    def configure_canvas(event):
        canvas_frame2.config(scrollregion=canvas_frame2.bbox("all"))

    frame2_inner.bind("<Configure>", configure_canvas)

    frame2_inner.pack(fill=tk.BOTH, expand=True)

    frame3 = tk.Frame(root, highlightthickness=1, highlightbackground="black")
    frame3.grid(row=1, column=2, columnspan=1, rowspan=10, pady=10, padx=10, sticky="nsew")

    frame4 = tk.Frame(root, highlightthickness=1, highlightbackground="black")
    frame4.grid(row=0, column=2, rowspan=1, pady=10, padx=10, sticky="nsew")

    frame5 = tk.Frame(root, highlightthickness=1, highlightbackground="black")
    frame5.grid(row=7, column=0, rowspan=10, pady=10, padx=10, sticky="nsew")

    # Adding scrollbar to frame5
    scrollbar_frame5 = tk.Scrollbar(frame5)
    scrollbar_frame5.pack(side=tk.RIGHT, fill=tk.Y)

    canvas_frame5 = tk.Canvas(frame5, highlightthickness=0, yscrollcommand=scrollbar_frame5.set)
    canvas_frame5.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar_frame5.config(command=canvas_frame5.yview)

    frame5_inner = tk.Frame(canvas_frame5)
    frame5_inner.grid_columnconfigure(0, weight=1, uniform="fixed")

    canvas_frame5.create_window((0, 0), window=frame5_inner, anchor=tk.NW)

    def configure_frame5(event):
        canvas_frame5.config(scrollregion=canvas_frame5.bbox("all"))

    frame5_inner.bind("<Configure>", configure_frame5)

    frame7 = tk.Frame(root, highlightthickness=1, highlightbackground="black")
    frame7.grid(row=10, column=0, rowspan=10, pady=10, padx=10, sticky="nsew")
    frame7.grid_columnconfigure(0, weight=1, uniform="fixed")


    frame6 = tk.Frame(root, width=width, height=height, bg='white', highlightthickness=1, highlightbackground="black")
    frame6.grid(row=1, column=1, padx=10, sticky="nsew")

    
    
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

    def delete_image(image_index):
        # Check if the image index is valid
        if 0 <= image_index < len(image_list):
            # Destroy the image widget
            image_list[image_index].destroy()
            
            # Destroy the associated delete button
            delete_image_list[image_index].destroy()
            
            # Destroy the associated update button
            update_image_list[image_index].destroy()

            # Remove the deleted image and its associated buttons from the lists
            del image_list[image_index]
            del delete_image_list[image_index]
            del update_image_list[image_index]

    def update_button_properties(button_index):

        # Get position in percentage from user input
        percentage_x = float(inyx_var.get().strip("%"))
        percentage_y = float(inyy_var.get().strip("%"))
        # Convert percentage values to pixels
        frame_width = frame2_inner.winfo_width()
        frame_height = frame2_inner.winfo_height()
        x = (percentage_x / 100) * frame_width
        y = (percentage_y / 100) * frame_height
        # Place the widget
        buttons_list[button_index].place(x=x, y=y)

        # Get the text from the text box
        new_text = text_var.get()
        # Update the text of the button
        buttons_list[button_index].configure(text=new_text)
        # Update background color
        buttons_list[button_index].configure(bg=bg_var.get())
        # Update foreground color
        buttons_list[button_index].configure(fg=fg_var.get())
        buttons_list[button_index].configure(font=(font_var.get(),font_size_var.get()))

    def update_label_properties(label_index):

        # Get position in percentage from user input
        percentage_x = float(inyx_var.get().strip("%"))
        percentage_y = float(inyy_var.get().strip("%"))
        # Convert percentage values to pixels
        frame_width = frame2_inner.winfo_width()
        frame_height = frame2_inner.winfo_height()
        x = (percentage_x / 100) * frame_width
        y = (percentage_y / 100) * frame_height
        # Place the widget
        labels_list[label_index].place(x=x, y=y)

        # Get the text from the text box
        new_text = text_var.get()
        # Update the text of the label
        labels_list[label_index].configure(text=new_text)
        # Update background color
        labels_list[label_index].configure(bg=bg_var.get())
        # Update foreground color
        labels_list[label_index].configure(fg=fg_var.get())
        
        labels_list[label_index].configure(font=(font_var.get(),font_size_var.get()))  # Change 12 to the desired font size


    def update_checkbox_properties(checkbox_index):

        # Get position in percentage from user input
        percentage_x = float(inyx_var.get().strip("%"))
        percentage_y = float(inyy_var.get().strip("%"))
        # Convert percentage values to pixels
        frame_width = frame2_inner.winfo_width()
        frame_height = frame2_inner.winfo_height()
        x = (percentage_x / 100) * frame_width
        y = (percentage_y / 100) * frame_height
        # Place the widget
        checkboxes_list[checkbox_index].place(x=x, y=y)

        # Get the text from the text box
        new_text = text_var.get()
        # Update the text of the checkbox
        checkboxes_list[checkbox_index].configure(text=new_text)
        # Update background color
        checkboxes_list[checkbox_index].configure(bg=bg_var.get())
        # Update foreground color
        checkboxes_list[checkbox_index].configure(fg=fg_var.get())
        checkboxes_list[checkbox_index].configure(font=(font_var.get(),font_size_var.get()))

    def update_image_properties(image_index):
        try:
            # Get position in percentage from user input
            percentage_x = float(inyx_var.get().strip("%"))
            percentage_y = float(inyy_var.get().strip("%"))
            # Convert percentage values to pixels
            frame_width = frame2_inner.winfo_width()
            frame_height = frame2_inner.winfo_height()
            x = (percentage_x / 100) * frame_width
            y = (percentage_y / 100) * frame_height
            # Place the widget
            image_list[image_index].place(x=x, y=y)

            # Get the new width and height from the entry fields
            new_width = int(img_width.get())
            new_height = int(img_height.get())

            # Open the image file
            image = Image.open(saved_image_path2)
            # Resize the image to the new dimensions
            resized_image = image.resize((new_width, new_height), Image.LANCZOS)
            # Convert the resized image to PhotoImage
            photo = ImageTk.PhotoImage(resized_image)
            # Update the image label with the resized image
            image_list[image_index].config(image=photo)
            image_list[image_index].image = photo  # Keep a reference to avoid garbage collection

        except Exception as e:
            print("Error updating image properties:", e)


    def add_button():
        index = len(buttons_list) + 1
        new_button = tk.Button(frame2_inner, text=f"Dynamic Button {index}")
        new_button.bind("<ButtonPress-1>", on_drag_start)
        new_button.bind("<B1-Motion>", on_drag_motion)
        new_button.bind("<ButtonRelease-1>", on_drag_end)

        new_button.pack()
        buttons_list.append(new_button)
        
        delete_button_button = tk.Button(frame5_inner,text=f"Delete Button {index}", command=lambda index=index-1: delete_buttons(index))
        delete_button_button.grid(column=1,sticky="nsew")
        delete_buttons_list.append(delete_button_button)

        update_button_properties_button = tk.Button(frame5_inner, text=f"Button Properties {index}", command=lambda index=index-1: update_button_properties(index))
        update_button_properties_button.grid(column=0,sticky="nsew")
        update_button_propertie.append(update_button_properties_button) 


    def add_label():
        index = len(labels_list) + 1
        new_label = tk.Label(frame2_inner, text=f"Dynamic Label {index}")
        new_label.bind("<ButtonPress-1>", on_drag_start)
        new_label.bind("<B1-Motion>", on_drag_motion)
        new_label.bind("<ButtonRelease-1>", on_drag_end)
        new_label.pack()
        labels_list.append(new_label)
        
        delete_label_button = tk.Button(frame5_inner, text=f"Delete Label {index}", command=lambda index=index-1: delete_labels(index))
        delete_label_button.grid(column=1,sticky="nsew")
        delete_labels_list.append(delete_label_button)

        update_label_properties_button = tk.Button(frame5_inner, text=f"Label Properties {index}", command=lambda index=index-1: update_label_properties(index))
        update_label_properties_button.grid(column=0,sticky="nsew")
        update_labels_propertie.append(update_label_properties_button)  # Append the update button to the list


    def add_checkbox():
        index = len(checkboxes_list) + 1
        new_checkbox = tk.Checkbutton(frame2_inner, text=f"Dynamic Checkbox {index}")
        new_checkbox.bind("<ButtonPress-1>", on_drag_start)
        new_checkbox.bind("<B1-Motion>", on_drag_motion)
        new_checkbox.bind("<ButtonRelease-1>", on_drag_end)
        new_checkbox.pack()
        checkboxes_list.append(new_checkbox)
        
        delete_checkbox_button = tk.Button(frame5_inner, text=f"Delete Checkbox {index}", command=lambda index=index-1: delete_checkboxes(index))
        delete_checkbox_button.grid(column=1,sticky="nsew")
        delete_checkboxes_list.append(delete_checkbox_button)

        update_checkboxes_properties_button = tk.Button(frame5_inner, text=f"Checkbox Properties {index}", command=lambda index=index-1: update_checkbox_properties(index))
        update_checkboxes_properties_button.grid(column=0,sticky="nsew")
        update_checkboxes_propertie.append(update_checkboxes_properties_button)  # Append the update button to the list


    
    
    header_frame=tk.Frame(frame2_inner)
    def add_header():

        label1 = tk.Label(header_frame, text="jobs", font=("Helvetica", 24), anchor="center", bg="purple")
        label2 = tk.Label(header_frame, text="Column 2", font=("Helvetica", 24), anchor="center")
        label3 = tk.Label(header_frame, text="Column 3", font=("Helvetica", 24), anchor="center")
        label4 = tk.Label(header_frame, text="Column 4", font=("Helvetica", 24), anchor="center")
        
        label1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        label2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        label3.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
        label4.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)
        
        header_frame.pack(fill="both", expand=True, padx=10, pady=10)
 

    def modify_header(lst):
            header_frame.destroy()

            frame=tk.Frame(frame2_inner)
            n=len(lst)
            print(len(lst))
            for i in range(n):
                frame.grid_columnconfigure(i, weight=1)
            for i in range(n):
                tk.Label(frame, text=lst[i],font=("Helvetica", 24), anchor="center").grid(row=0, column=i, sticky="nsew")
            frame.pack(fill="both")  
    def add_image():   
        global file_path1  # Use the global keyword to access the global file_path variable
        # Ask the user to select an image file
        file_path1 = filedialog.askopenfilename()
        
        if file_path1:
            global saved_image_path2
            # Display the image
            display_image_frame2(file_path1)
            # Save the image to the file folder
            save_new_image(file_path1)
            # Add delete and update buttons for the image

    def save_new_image(file_path1):
        global saved_image_path2
        directory = "E:\\openbrackets-styles-\\"
        os.makedirs(directory, exist_ok=True)
        file_name1 = os.path.basename(file_path1)
        destination = os.path.join(directory, file_name1)
        try:
            shutil.copyfile(file_path1, destination)
            # Update the global variable with the saved image path
            saved_image_path2 = file_name1
            destination.replace("\\", "/")  # Print the file path in the desired format
            return destination  # Return the destination path
        except Exception as e:
            print("Error saving the image:", e)
            return ""  # Return an empty string if there's an error

    def display_image_frame2(file_path1):

        index = len(image_list) + 1
        pic2box = tk.Label(frame2_inner)
        pic2box.bind("<ButtonPress-1>", on_drag_start)
        pic2box.bind("<B1-Motion>", on_drag_motion)
        pic2box.bind("<ButtonRelease-1>", on_drag_end)
        pic2box.pack() 
        image_list.append(pic2box)   

        try:
            # Open the image file
            image = Image.open(file_path1)
            # Resize the image to fit the dimensions of picbox
            width, height = pic2box.winfo_width(), pic2box.winfo_height()
            image = image.resize((width, height), Image.LANCZOS)
            # Convert the resized image to PhotoImage
            photo = ImageTk.PhotoImage(image)
            # Update the picbox with the resized image
            picbox.config(image=photo)
            picbox.image = photo  # Keep a reference to avoid garbage collection
        except Exception as e:
            print("Error opening or displaying image:", e)

        delete_button = tk.Button(frame5_inner, text=f"Delete Image {index}", command=lambda index=index-1: delete_image(index))
        delete_button.grid(row=index, column=1, sticky="nsew")
        
        update_button = tk.Button(frame5_inner, text=f"Image Properties {index}", command=lambda index=index-1: update_image_properties(index))
        update_button.grid(row=index, column=0, sticky="nsew")

        # Append the buttons to their respective lists
        delete_image_list.append(delete_button)
        update_image_list.append(update_button)

    button_add_button = tk.Button(frame1, text="Add Button", command=add_button)
    button_add_button.pack()

    button_add_label = tk.Button(frame1, text="Add Label", command=add_label)
    button_add_label.pack()

    button_add_checkbox = tk.Button(frame1, text="Add Checkbox", command=add_checkbox)
    button_add_checkbox.pack()

    button_add_image = tk.Button(frame1, text="Add Image", command=add_image)
    button_add_image.pack()

    add_header_button= tk.Button(frame1, text="Add Header", command=lambda: add_header())
    add_header_button.pack()

    def convert_to_html():
        # Call the convert_frame2_details_to_html function and pass the file_path
        html.convert_frame2_details_to_html(frame2_inner, frame6, saved_image_path,saved_image_path2)
        css.convert_frame2_details_to_css(frame2_inner,background_var.get(),saved_image_path,saved_image_path2)
        print(f"{saved_image_path}")
        print(f"{saved_image_path2}")


    button_f = tk.Button(frame4, text="Convert to HTML", command=lambda: convert_to_html())
    button_f.pack()

    button_close = tk.Button(frame4, text="Close App", command=root.destroy)
    button_close.pack()

    title_var = tk.StringVar(value="ENTER WEB TITLE HERE")

    title_entry = tk.Entry(frame6,width=50, textvariable=title_var)
    title_entry.grid(row=0, column=0,padx=10,pady=10, sticky="nsew")

    background = tk.Canvas(frame6, width=40, height=20, bg="white", highlightthickness=0)
    background.grid(row=1, column=0, padx=(5, 0), sticky="w")

    open_button = tk.Button(frame6, text="Open Image", command=open_image)
    open_button.grid(row=2, column=0, padx=(5, 0), sticky="w")

    # Create a label widget to display the image
    picbox = tk.Label(frame6,width=18,height=12)
    picbox.grid(row=2, column=1, padx=(5, 0), sticky="w")

    bg_canvas = tk.Canvas(frame3, width=40, height=20, bg="white", highlightthickness=0)
    bg_canvas.grid(row=1, column=3, padx=(5, 0), sticky="w")

    fg_canvas = tk.Canvas(frame3, width=40, height=20, bg="white", highlightthickness=0)
    fg_canvas.grid(row=2, column=3, padx=(5, 0), sticky="w")

    def open_color_picker_and_update_canvas(variable, canvas):
        color = colorchooser.askcolor()[1]
        if color:
            variable.set(color)
            canvas.configure(bg=color)

    notebook = ttk.Notebook(frame3)
    notebook.grid(row=0, column=0, columnspan=4, rowspan=3, sticky="nsew")

    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text='Details')

    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text='Transform')

    tab3 = ttk.Frame(notebook)
    notebook.add(tab3, text='Header')

    # Entry and buttons for modifying properties
    text_var = tk.StringVar(value="NEW ITEM")
    background_var=tk.StringVar(value ="white")
    bg_var = tk.StringVar(value ="black")
    fg_var = tk.StringVar(value = "white")
    inyx_var = tk.StringVar(value="0")
    inyy_var = tk.StringVar(value="0")
    font_var=tk.StringVar()
    font_size_var=tk.IntVar()
    img_width=tk.StringVar(value="0")
    img_height=tk.StringVar(value="0")

    
    tk.Label(tab1, text="Fontsize:").grid(row=4, column=0, sticky='w')
    font_entry= tk.Entry(tab1,textvariable=font_size_var)
    font_entry.grid(row=4, column=1,columnspan=4,sticky="w")
    
    tk.Label(tab1, text="Text:").grid(row=0, column=0, sticky='w')
    text_entry = tk.Entry(tab1, textvariable=text_var)
    text_entry.grid(row=0, column=1, sticky="w")

    background_canvas = tk.Canvas(frame6, width=40, height=20, bg="white", highlightthickness=0)
    background_canvas.grid(row=1, column=2, padx=(5, 0), sticky="w")

    bg_canvas_tab1 = tk.Canvas(tab1, width=40, height=20, bg="black", highlightthickness=0)
    bg_canvas_tab1.grid(row=1, column=2, padx=(5, 0), sticky="w")

    fg_canvas_tab1 = tk.Canvas(tab1, width=40, height=20, bg="white", highlightthickness=0)
    fg_canvas_tab1.grid(row=2, column=2, padx=(5, 0), sticky="w")

    background_button = tk.Button(frame6, text="Page Color", command=lambda: open_color_picker_and_update_canvas(background_var, background_canvas))
    background_button.grid(row=1, column=0,columnspan=10, padx=(5, 0), sticky="w")

    bg_button_tab1 = tk.Button(tab1, text="Background Color", command=lambda: open_color_picker_and_update_canvas(bg_var, bg_canvas_tab1))
    bg_button_tab1.grid(row=1, column=0,columnspan=10, padx=(5, 0), sticky="w")

    fg_button_tab1 = tk.Button(tab1, text="Foreground Color", command=lambda: open_color_picker_and_update_canvas(fg_var, fg_canvas_tab1))
    fg_button_tab1.grid(row=2, column=0,columnspan=10, padx=(5, 0), sticky="w")

    delete_last = tk.Button(frame7, text="Delete", command=lambda:delete_last_item(len(frame2_inner.winfo_children()) - 1))
    delete_last.grid(row=0, column=0,columnspan=10, padx=(5, 0), sticky="w")
    
    update_last = tk.Button(frame7, text="Update", command=lambda: update_last_item(len(frame2_inner.winfo_children()) - 1))
    update_last.grid(row=0, column=2, columnspan=10, padx=(5, 5), sticky="w")

    tk.Label(tab2, text="X Position:-").grid(row=0, column=0, sticky='w')
    x_entry = tk.Entry(tab2, textvariable=inyx_var)
    x_entry.grid(row=0, column=1, sticky="w")

    tk.Label(tab2, text="Y Position:-").grid(row=1, column=0, sticky='w')
    x_entry = tk.Entry(tab2, textvariable=inyy_var)
    x_entry.grid(row=1, column=1, sticky="w")

    tk.Label(tab2, text="Image Width:-").grid(row=3, column=0, sticky='w')
    x_entry = tk.Entry(tab2, textvariable=img_width)
    x_entry.grid(row=3, column=1, sticky="w")

    tk.Label(tab2, text="Image Height:-").grid(row=4, column=0, sticky='w')
    x_entry = tk.Entry(tab2, textvariable=img_height)
    x_entry.grid(row=4, column=1, sticky="w")
    
    def modify_header_helper(str_lst):
        for i in str_lst:
            entry_list.append(i.get())
        print("List",entry_list)  
        modify_header(entry_list)

    def update_entries():
        for entry in entry_list:
            entry.grid_forget()

        # Get the new count

        new_count = count.get()
        str_lst=[]
        # Create new entries
        for i in range(new_count):
            str=tk.StringVar()
            entry = tk.Entry(tab3,textvariable=str)
            entry.grid(row=i+2, column=0, sticky="w")
            str_lst.append(str)
        tk.Button(tab3, text="reflect", command=lambda: modify_header_helper(str_lst)).grid(row=new_count+1, column=0, columnspan=2)

    count = tk.IntVar(value=0)
    entry_list = []

    tk.Label(tab3, text="Number:").grid(row=0, column=0, sticky='w')
    x_entry = tk.Entry(tab3, textvariable=count)
    x_entry.grid(row=0, column=1, sticky="w")

    update_btn = tk.Button(tab3, text="Update Entries", command=update_entries)
    update_btn.grid(row=1, column=0, columnspan=2)


    
    """def on_select(*args):
        selected_item = selected_item_var.get()"""
        
    #code for the font chooser in gui
    
    fontlist=[]
    for f in font.families():
        fontlist.append(f)
    tk.Label(tab1, text="Font:").grid(row=3, column=0, sticky='w')
    font_var.set(fontlist[0])
    font_listbox = tk.OptionMenu(tab1,font_var,*fontlist)
    font_listbox.grid(row=3, column=1, padx=(5, 0), sticky="w")
    
    tk.Label(tab1, text="Fontsize:").grid(row=4, column=0, sticky='w')
    

    
    
    def delete_last_item(last_index):
        # Check if there are any widgets in frame2_inner
        if frame2_inner.winfo_children():
            # Get the last widget and destroy it
            last_widget = frame2_inner.winfo_children()[-1]
            last_widget.destroy()
            # Also, remove the associated delete button and update button from their respective lists
            if isinstance(last_widget, tk.Button):
                buttons_list[last_index].destroy()
                delete_buttons_list[last_index].destroy()
                update_button_propertie[last_index].destroy()
                # Remove the deleted buttons from the lists
                del buttons_list[last_index]
                del delete_buttons_list[last_index]
                del update_button_propertie[last_index]
            elif isinstance(last_widget, tk.Label):
                labels_list[last_index].destroy()
                delete_labels_list[last_index].destroy()
                update_labels_propertie[last_index].destroy()
                # Remove the deleted labels and their associated delete buttons from the lists
                del labels_list[last_index]
                del delete_labels_list[last_index]
                del update_labels_propertie[last_index]
            elif isinstance(last_widget, tk.Checkbutton):
                checkboxes_list[last_index].destroy()
                delete_checkboxes_list[last_index].destroy()
                update_checkboxes_propertie[last_index].destroy()
                # Remove the deleted checkboxes and their associated delete buttons from the lists
                del checkboxes_list[last_index]
                del delete_checkboxes_list[last_index]
                del update_checkboxes_propertie[last_index]

    def update_last_item(last_index):
        # Check if there are any widgets in frame2_inner
        if frame2_inner.winfo_children():
            # Get the last widget
            last_widget = frame2_inner.winfo_children()[-1]

            frame2_inner.configure(bg=background_var.get())

            global file_path
            if file_path:  # Check if file_path is not empty
                try:
                    # Open the image file using the global file_path variable
                    image = Image.open(file_path)
                    # Resize the image to fit the dimensions of the canvas (frame2_inner)
                    width, height = frame2_inner.winfo_width(), frame2_inner.winfo_height()
                    image = image.resize((width, height), Image.LANCZOS)
                    # Convert the resized image to PhotoImage
                    photo = ImageTk.PhotoImage(image)
                    # Update the canvas with the resized image
                    image_label.configure(image=photo)
                    image_label.image = photo  # Keep a reference to avoid garbage collection
                except Exception as e:
                    print("Error opening or displaying image:", e)
        
            # Implement the logic to update properties of the last widget here
            if isinstance(last_widget, tk.Button):
                # Get the text from the text box
                new_text = text_var.get()
                # Update the text of the button
                buttons_list[last_index].configure(text=new_text)
                # Update background color
                buttons_list[last_index].configure(bg=bg_var.get())
                # Update foreground color
                buttons_list[last_index].configure(fg=fg_var.get())

                # Get position in percentage from user input
                percentage_x = float(inyx_var.get().strip("%"))
                percentage_y = float(inyy_var.get().strip("%"))
                # Convert percentage values to pixels
                frame_width = frame2_inner.winfo_width()
                frame_height = frame2_inner.winfo_height()
                x = (percentage_x / 100) * frame_width
                y = (percentage_y / 100) * frame_height
                # Place the widget
                buttons_list[last_index].place(x=x, y=y)
                buttons_list[last_index].configure(font=(font_var.get(),font_size_var.get()))


            elif isinstance(last_widget, tk.Label):
                # Get the text from the text box
                new_text = text_var.get()
                # Update the text of the label
                labels_list[last_index].configure(text=new_text)
                # Update background color
                labels_list[last_index].configure(bg=bg_var.get())
                # Update foreground color
                labels_list[last_index].configure(fg=fg_var.get())

                # Get position in percentage from user input
                percentage_x = float(inyx_var.get().strip("%"))
                percentage_y = float(inyy_var.get().strip("%"))
                # Convert percentage values to pixels
                frame_width = frame2_inner.winfo_width()
                frame_height = frame2_inner.winfo_height()
                x = (percentage_x / 100) * frame_width
                y = (percentage_y / 100) * frame_height
                # Place the widget
                labels_list[last_index].place(x=x, y=y)
                labels_list[last_index].configure(font=(font_var.get(),font_size_var.get()))  # Change 12 to the desired font size


            elif isinstance(last_widget, tk.Checkbutton):
                # Get the text from the text box
                new_text = text_var.get()
                # Update the text of the checkbox
                checkboxes_list[last_index].configure(text=new_text)
                # Update background color
                checkboxes_list[last_index].configure(bg=bg_var.get())
                # Update foreground color
                checkboxes_list[last_index].configure(fg=fg_var.get())

                # Get position in percentage from user input
                percentage_x = float(inyx_var.get().strip("%"))
                percentage_y = float(inyy_var.get().strip("%"))
                # Convert percentage values to pixels
                frame_width = frame2_inner.winfo_width()
                frame_height = frame2_inner.winfo_height()
                x = (percentage_x / 100) * frame_width
                y = (percentage_y / 100) * frame_height
                # Place the widget
                checkboxes_list[last_index].place(x=x, y=y)
                checkboxes_list[last_index].configure(font=(font_var.get(),font_size_var.get()))


            # Also update corresponding buttons in frame5_inner
            if isinstance(last_widget, (tk.Button, tk.Label, tk.Checkbutton)):
                update_buttons_in_frame5(last_index)

    def update_buttons_in_frame5(last_index):
        # Update the properties of corresponding buttons in frame5_inner
        if len(frame5_inner.winfo_children()) > last_index:
            update_button = update_button_propertie[last_index]
            update_button.configure(text=f"Button Properties {last_index + 1}")  # Update text of the button
            # Associate with the updated update function
            update_button.configure(command=lambda index=last_index: update_last_item(index))




    root.mainloop()