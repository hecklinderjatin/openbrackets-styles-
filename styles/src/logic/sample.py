import tkinter as tk

def update_html_content():
    # Read values from Tkinter variables
    names = names_listbox.get(0, tk.END)
    age_value = age_var.get()

    # Generate HTML content with Tkinter variable values
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User Information</title>
    </head>
    <body>
        <h1>User Information</h1>
    """
    
    for name in names:
        html_content += f"<p>Name: {name}</p>\n"
        
    html_content += f"<p>Age: {age_value}</p>\n</body>\n</html>"

    # Write HTML content to a file
    with open("user_info.html", "w") as f:
        f.write(html_content)

def add_name():
    name = name_var.get()
    names_listbox.insert(tk.END, name)
    name_var.set("")

# Create Tkinter window
window = tk.Tk()
window.title("Tkinter to HTML")

# Create Tkinter variables+
name_var = tk.StringVar()
age_var = tk.IntVar()

# Create Tkinter widgets
name_label = tk.Label(window, text="Name:")
name_entry = tk.Entry(window, textvariable=name_var)
age_label = tk.Label(window, text="Age:")
age_entry = tk.Entry(window, textvariable=age_var)
add_name_button = tk.Button(window, text="Add Name", command=add_name)
generate_button = tk.Button(window, text="Generate HTML", command=update_html_content)
names_listbox = tk.Listbox(window)

# Layout Tkinter widgets
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
add_name_button.grid(row=0, column=2)
age_label.grid(row=1, column=0)
age_entry.grid(row=1, column=1)
generate_button.grid(row=2, columnspan=3)
names_listbox.grid(row=3, columnspan=3)

# Run Tkinter event loop
window.mainloop()