import tkinter as tk


def convert_frame2_details_to_html(frame2):
    html_details = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User Input</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <h1>User Input</h1>
    """

    children = frame2.winfo_children()
    for child in children:
        if isinstance(child, tk.Button):  # Change to standard tkinter Button
            html_details += f"<button class='{child.cget('text').lower()}'>{child.cget('text')}</button><br>\n"
        elif isinstance(child, tk.Label):  # Change to standard tkinter Label
            html_details += f"<label class='{child.cget('text').lower()}'>{child.cget('text')}</label><br>\n"
        elif isinstance(child, tk.Checkbutton):  # Change to standard tkinter Checkbutton
            html_details += f"""<input type="checkbox" class='{child.cget('text').lower()}'>
  <label class='{child.cget('text').lower()}'>{child.cget('text')}</label><br>\n"""

    html_details += "\n</body>\n</html>"

    # Save HTML details to an HTML file
    with open("output.html", "w") as html_file:
        html_file.write(html_details)
