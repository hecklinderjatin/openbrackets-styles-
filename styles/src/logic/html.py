import tkinter as tk
import customtkinter as ctk

def convert_frame2_details_to_html(frame2):
    html_details = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User Input</title>
        <link rel="stylesheet" type="text/css" href="styles.css">
    </head>
    <body>
        <h1>User Input</h1>
    """

    css_details = ""  # Initialize CSS details string

    children = frame2.winfo_children()
    for child in children:
        if isinstance(child, ctk.CTkButton):
            html_details += f"<button class='{child.cget('text').lower()}'>{child.cget('text')}</button><br>"
            css_details += f".{child.cget('text').lower()} {{ /* Button style for {child.cget('text')} */ }}\n"
        elif isinstance(child, ctk.CTkLabel):
            html_details += f"<label class='{child.cget('text').lower()}'>{child.cget('text')}</label><br>"
            css_details += f".{child.cget('text').lower()} {{ /* Label style for {child.cget('text')} */ }}\n"
        elif isinstance(child, ctk.CTkCheckBox):
            html_details += f"""<input type="checkbox" class='{child.cget('text').lower()}'>
  <label class='{child.cget('text').lower()}'>{child.cget('text')}</label><br>"""
            css_details += f".{child.cget('text').lower()} {{ /* Checkbox style for {child.cget('text')} */ }}\n"

    html_details += "</body></html>"

    # Save HTML details to an HTML file
    with open("output.html", "w") as html_file:
        html_file.write(html_details)

    # Save CSS details to a CSS file
    with open("styles.css", "w") as css_file:
        css_file.write(css_details)
