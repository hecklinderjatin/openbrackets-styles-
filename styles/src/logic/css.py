import tkinter as tk
import tkinter.font as tkfont 
import re

def convert_frame2_details_to_css(frame3, page_color, background_image_path,frame2_url):
    css_details = ""  # Initialize CSS details string
    i = -1
    children = frame3.winfo_children()
    for child in children:
        if hasattr(child, 'cget') and 'text' in child.keys():  # Check if the widget has 'text' option
            css_class = child.cget('text').lower().replace(" ", "-")  # Generate a CSS class from the element's text
            css_details += f".{css_class}{i}{{\n"  # Start defining CSS for the class
            # Extract and include properties of buttons, labels, and checkboxes
            if isinstance(child, tk.Button):
                css_details += f"    background-color: {child.cget('bg')};\n"
                css_details += f"    color: {child.cget('fg')};\n"
                css_details += f"    /* Button style for {child.cget('text')} */\n"
                css_details += f"    position: absolute;\n"
                css_details += f"    left:{int(child.winfo_x())*0.21}%;\n"
                css_details += f"    top:{int(child.winfo_y())*0.21}%;\n"

                font_string = child.cget('font')
                # Use regular expressions to extract the font size
                font_size_match = re.search(r'\d+', font_string)
                if font_size_match:
                    font_size = int(font_size_match.group()) * 3
                else:
                    # Handle the case where the font size is not found
                    font_size = 12  # Default font size

                css_details += f"    font-size: {font_size}px;\n"

                font_family = child.cget('font').split(' ')[0]
                css_details += f"    font-family: {font_family};\n"

            elif isinstance(child, tk.Label):
                    css_details += f"    background-color: {child.cget('bg')};\n"
                    css_details += f"    color: {child.cget('fg')};\n"
                    css_details += f"    /* Button style for {child.cget('text')} */\n"
                    css_details += f"    position: absolute;\n"
                    css_details += f"    left:{int(child.winfo_x())*0.21}%;\n"
                    css_details += f"    top:{int(child.winfo_y())*0.21}%;\n"

                    font_string = child.cget('font')
                    # Use regular expressions to extract the font size
                    font_size_match = re.search(r'\d+', font_string)
                    if font_size_match:
                        font_size = int(font_size_match.group()) * 3
                    else:
                        # Handle the case where the font size is not found
                        font_size = 12  # Default font size

                    css_details += f"    font-size: {font_size}px;\n"

                    font_family = child.cget('font').split(' ')[0]
                    css_details += f"    font-family: {font_family};\n"

            elif isinstance(child, tk.Checkbutton):
                    css_details += f"    background-color: {child.cget('bg')};\n"
                    css_details += f"    color: {child.cget('fg')};\n"
                    css_details += f"    /* Button style for {child.cget('text')} */\n"
                    css_details += f"    position: absolute;\n"
                    css_details += f"    left:{int(child.winfo_x())*0.21}%;\n"
                    css_details += f"    top:{int(child.winfo_y())*0.21}%;\n"

                    font_string = child.cget('font')
                    # Use regular expressions to extract the font size
                    font_size_match = re.search(r'\d+', font_string)
                    if font_size_match:
                        font_size = int(font_size_match.group()) * 3
                    else:
                        # Handle the case where the font size is not found
                        font_size = 12  # Default font size

                    css_details += f"    font-size: {font_size}px;\n"

                    font_family = child.cget('font').split(' ')[0]
                    css_details += f"    font-family: {font_family};\n"
            i += 1

        css_details += "}\n\n"  # End of CSS class definition

    # Include page color
    css_details += f"body {{\n"
    css_details += f"    background-color: {page_color};\n"
    css_details += f"}}\n\n"


    # Save CSS details to a CSS file
    with open("styles.css", "w") as css_file:
        css_file.write(css_details)
