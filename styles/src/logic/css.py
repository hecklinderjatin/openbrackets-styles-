
import customtkinter as ctk


def convert_frame2_details_to_css(frame2):


    css_details = ""  # Initialize CSS details string

    children = frame2.winfo_children()
    for child in children:
        if isinstance(child, ctk.CTkButton):
            css_details += f".{child.cget('text').lower()} {{ /* Button style for {child.cget('text')} */ }}\n"
        elif isinstance(child, ctk.CTkLabel):
            css_details += f".{child.cget('text').lower()} {{ /* Label style for {child.cget('text')} */ }}\n"
        elif isinstance(child, ctk.CTkCheckBox):
            css_details += f".{child.cget('text').lower()} {{ /* Checkbox style for {child.cget('text')} */ }}\n"



    # Save CSS details to a CSS file
    with open("styles.css", "w") as css_file:
        css_file.write(css_details)