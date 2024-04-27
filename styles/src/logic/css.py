import tkinter as tk
import tkinter.font as tkfont 

import re



def convert_frame2_details_to_css(frame2_inner,new_frame, page_color, background_image_path,frame2_url):
    css_details = ""
    k=1

    # Include page color
    css_details += f"body {{\n"
    css_details += f"    background-color: {page_color};\n"
    css_details += f"}}\n\n"

    for child in new_frame.winfo_children():
        if isinstance(child, tk.Label):
                css_details += ".navbar{\n"
                css_details += f"    display: flex;\n"
                css_details += f"    justify-content: space-between;\n"
                css_details += f"    align-items: center;\n"
                css_details += f"    height: 50px;\n"
                css_details += f"    background-color: {child.cget('bg')};\n"
                css_details += f"    color: {child.cget('fg')};\n"
                css_details += "}\n"

                css_details += ".nav-item{\n"
                css_details += f"    flex: 1;\n"
                css_details += f"    height: 100%;\n"
                css_details += f"    display: flex;\n"
                css_details += f"    justify-content: center;\n"
                css_details += f"    align-items: center;\n"
                css_details += f"    font-size: 20 px;\n"


                k=0
                break


    if k==0:
        css_details += "}\n"

    i = 0
    children = frame2_inner.winfo_children()
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
                css_details += f"    left:{int(child.winfo_x())*0.111}%;\n"
                css_details += f"    top:{int(child.winfo_y())*0.211}%;\n"

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
                    css_details += f"    left:{int(child.winfo_x())*0.111}%;\n"
                    css_details += f"    top:{int(child.winfo_y())*0.211}%;\n"

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
                    css_details += f"    left:{int(child.winfo_x())*0.111}%;\n"
                    css_details += f"    top:{int(child.winfo_y())*0.211}%;\n"

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

    if frame2_url:
        j = 0 # Initialize counter for image CSS classes
        children = frame2_inner.winfo_children()  # Get all children of frame2_inner
        for child in children[1:]:  # Start iterating from the second child
            if isinstance(child, tk.Label):  # Check if the widget is a Label
                css_details += f".image{j} {{\n"  # Start CSS class definition for image
                # Get width and height of the image
                width = child.winfo_width()
                height = child.winfo_height()
                # Calculate and include position relative to the parent frame
                css_details += f"    width: {width}px;\n"
                css_details += f"    height: {height}px;\n"
                css_details += f"    left: {int(child.winfo_x()) * 0.111}% ;\n"
                css_details += f"    top: {int(child.winfo_y()) * 0.211}%;\n"
                css_details += f"    position: absolute;\n"

                css_details += "}\n\n"  # End of CSS class definition
                j += 1  # Increment image counter


            
    
    with open("styles.css", "w") as css_file:
        css_file.write(css_details)
