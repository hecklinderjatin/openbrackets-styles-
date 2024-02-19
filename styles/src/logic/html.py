# html.py

import tkinter as tk
import customtkinter as ctk
from logic import functions  # Correct import statement

def convert_frame2_details_to_html(frame2):
    details = ""
    children = frame2.winfo_children()
    for child in children:
        details += f"{child.cget('text')}<br>"
    
    # Save details to an HTML file
    with open("output.html", "w") as html_file:
        html_file.write("<html><body>")
        html_file.write(details)
        html_file.write("</body></html>")
