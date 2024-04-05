import tkinter as tk

def convert_frame2_details_to_css(frame3):
    css_details = ""  # Initialize CSS details string
    i=0
    children = frame3.winfo_children()
    for child in children:
        css_class = child.cget('text').lower().replace(" ", "-")  # Generate a CSS class from the element's text
        css_details += f".{css_class}{i}{{\n"  # Start defining CSS for the class
        i+=1
        # Extract and include properties of buttons, labels, and checkboxes
        if isinstance(child, tk.Button):
            css_details += f"    background-color: {child.cget('bg')};\n"
            css_details += f"    color: {child.cget('fg')};\n"
            css_details += f"    /* Button style for {child.cget('text')} */\n"
        elif isinstance(child, tk.Label):
            css_details += f"    background-color: {child.cget('bg')};\n"
            css_details += f"    color: {child.cget('fg')};\n"
            css_details += f"    /* Label style for {child.cget('text')} */\n"
        elif isinstance(child, tk.Checkbutton):
            css_details += f"    background-color: {child.cget('bg')};\n"
            css_details += f"    color: {child.cget('fg')};\n"
            css_details += f"    /* Checkbox style for {child.cget('text')} */\n"

        css_details += "}\n\n"  # End of CSS class definition

    # Save CSS details to a CSS file
    with open("styles.css", "w") as css_file:
        css_file.write(css_details)
