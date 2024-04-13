import tkinter as tk
from PIL import Image, ImageTk

def convert_frame2_details_to_html(frame2, frame6, background_image_url, image_path):
    
    html_details = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                background-image: url('{background_image_url}');
                background-repeat: no-repeat;
            }}
        </style>
    """

    # Extract title from Entry widget in frame6
    title = None
    for child in frame6.winfo_children():
        if isinstance(child, tk.Entry):
            title = child.get()
            break

    # If title exists, add it to HTML
    if title:
        html_details += f"<title>{title}</title>\n"
    
    html_details += """
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
    """

    for child in frame2.winfo_children():
        if isinstance(child, tk.Button):
            html_details += f"<button class='{child.cget('text').lower().replace(' ', '-')}'>{child.cget('text')}</button><br>\n"
        elif isinstance(child, tk.Label):
            html_details += f"<label class='{child.cget('text').lower().replace(' ', '-')}'>{child.cget('text')}</label><br>\n"
        elif isinstance(child, tk.Checkbutton):
            html_details += f"""<input type="checkbox" class='{child.cget('text').lower().replace(' ', '-')}'>
            <label class='{child.cget('text').lower().replace(' ', '-')}'>{child.cget('text')}</label><br>\n"""
        html_details += f"<img src='{image_path}'>\n"


    html_details += "\n</body>\n</html>"

    # Save HTML details to an HTML file
    with open("output.html", "w") as html_file:
        html_file.write(html_details)
