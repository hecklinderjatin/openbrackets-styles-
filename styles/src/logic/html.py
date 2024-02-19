# html.py

import tkinter as tk
import customtkinter as ctk

def convert_frame2_details_to_html(frame2):
    details = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User Input</title>
    </head>
    <body>
        <h1>User Input</h1>
    """
    
    children = frame2.winfo_children()
    for child in children:
        if isinstance(child, ctk.CTkButton):
            details += f"<button>{child.cget('text')}</button><br>"
        elif isinstance(child, ctk.CTkLabel):
            details += f"<label>{child.cget('text')}</label><br>"
        elif isinstance(child, ctk.CTkCheckBox):
            details += f"""<input type="checkbox">
  <label>{child.cget('text')}</label><br>"""


    details += "</body></html>"
    
    # Save details to an HTML file
    with open("output.html", "w") as html_file:
        html_file.write(details)
