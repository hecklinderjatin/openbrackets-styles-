import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        display_image(file_path)

def display_image(file_path):
    image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo

# Create the main application window
root = tk.Tk()
root.title("Image Viewer")

# Create a button to open the file dialog
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

# Create a label widget to display the image
label = tk.Label(root)
label.pack()

# Run the Tkinter event loop
root.mainloop()
