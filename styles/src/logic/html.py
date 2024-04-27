import tkinter as tk

def convert_frame2_details_to_html(frame2_inner,new_frame, frame6, background_image_url, image_path):
    
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
    k=1
    html_details += f"<div class='navbar'>\n"
    for child in new_frame.winfo_children():
        if isinstance(child, tk.Label):
            html_details += f"     <div class='nav-item'>{child.cget('text').lower()}</div>\n"
            k=0
    if k==0:
        html_details += f"</div>\n"


    i = 0
    for child in frame2_inner.winfo_children():
        if isinstance(child, tk.Button):
            html_details += f"<button class='{child.cget('text').lower().replace(' ', '-')}{i}'>{child.cget('text')}</button><br>\n"
        elif isinstance(child, tk.Label):
                html_details += f"<label class='{child.cget('text').lower().replace(' ', '-')}{i}'>{child.cget('text')}</label><br>\n"
        elif isinstance(child, tk.Checkbutton):
            html_details += f"""<input type="checkbox" class='{child.cget('text').lower().replace(' ', '-')}'>
            <label class='{child.cget('text').lower().replace(' ', '-')}{i}'>{child.cget('text')}</label><br>\n"""
        i+=1

    j=0
    for child in frame2_inner.winfo_children():
        if isinstance(child, tk.Label):
            if image_path:
                html_details += f"""<img src="{image_path}" class = "image{j}">\n"""
                j+=1
                break
        
  


    html_details += "\n</body>\n</html>"

    # Save HTML details to an HTML file
    with open("output.html", "w") as html_file:
        html_file.write(html_details)
