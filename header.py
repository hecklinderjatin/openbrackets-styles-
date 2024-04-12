# import tkinter as tk

# root = tk.Tk()

# count=tk.IntVar(value=0)
# lst=[]
# def print_coloum():
#         pass

# def helper():
#          str=tk.StringVar()
       
#          for i in range(count.get()):
#              tk.Entry(root, textvariable=str).grid(row=i+2, column=0, sticky="w")
#              lst.append(str.get())
#          refelect= tk.Button(root, text="reflect", command=lambda:print_coloum)
#          refelect.grid(row=5,column=1)   

# tk.Label(root, text="Number:-").grid(row=0, column=0, sticky='w')
# x_entry = tk.Entry(root, textvariable=count).grid(row=0, column=1, sticky="w")
# saveheader= tk.Button(root, text="reflect", command=lambda:helper)
# saveheader.grid(row=1,column=0)  

# root.mainloop()

import tkinter as tk

# def update_entries():
    # Clear the existing entries
#     for entry in entry_list:
#         entry.grid_forget()
    
#     # Get the new count
#     new_count = count.get()
    
#     # Create new entries
#     for i in range(new_count):
#         entry = tk.Entry(root)
#         entry.grid(row=i+2, column=0, sticky="w")
#         entry_list.append(entry)
#     tk.Button(root, text="reflect", command=).grid(row=new_count+1, column=0, columnspan=2)
   

# root = tk.Tk()

# count = tk.IntVar(value=0)
# entry_list = []

# tk.Label(root, text="Number:").grid(row=0, column=0, sticky='w')
# x_entry = tk.Entry(root, textvariable=count)
# x_entry.grid(row=0, column=1, sticky="w")

# update_btn = tk.Button(root, text="Update Entries", command=update_entries)
# update_btn.grid(row=1, column=0, columnspan=2)

# root.mainloop()

def modify_header(lst):
           
         root=tk.Tk()

         n=len(lst)
         for i in range(n):
            root.grid_columnconfigure(i, weight=1)
         for i in range(n):
           tk.Label(root, text=lst[i],font=("Helvetica", 24), anchor="center").grid(row=0, column=i, sticky="nsew")

         root.mainloop()  

modify_header(["raji","nama","nsjw"])





# import tkinter as tk
# from tkinter import ttk

# def create_header(tree):
#     # Define the header labels
#     headers = ["Column 1", "Column 2", "Column 3", "Column 4"]

#     # Configure the treeview columns
#     tree["columns"] = headers
#     for header in headers:
#         tree.heading(header, text=header)
#         tree.column(header, width=100)  # Adjust column width as needed

# def main():
#     root = tk.Tk()
#     root.title("Website Header with Columns")
#     root.geometry("400x200")

#     # Create a treeview widget for the header
#     header_tree = ttk.Treeview(root, show="headings",bg="purple")
#     create_header(header_tree)


#     header_tree.pack(fill="both", expand=True)

#     root.mainloop()

# if __name__ == "__main__":
#     main()

# import tkinter as tk
# from tkinter import ttk

# def create_header(tree):
#     # Define the header labels
#     headers = ["Column 1", "Column 2", "Column 3", "Column 4"]

#     # Configure the treeview columns
#     tree["columns"] = headers
#     for header in headers:
#         tree.heading(header, text=header)
#         tree.column(header, width=100)  # Adjust column width as needed

# def main():
#     root = tk.Tk()
#     root.title("Website Header with Columns")
#     root.geometry("400x200")

#     # Create a treeview widget for the header
#     header_tree = ttk.Treeview(root, show="headings")
#     create_header(header_tree)

#     # Customize the column colors
#     header_tree.tag_configure("odd_row", background="lightblue")
#     header_tree.tag_configure("even_row", background="lightgreen")

#     # Add sample data (you can replace this with your actual data)
#     for i in range(10):
#         values = [f"Value {i+1}"] * 4
#         header_tree.insert("", tk.END, values=values, tags=("odd_row",) if i % 2 == 0 else ("even_row",))

#     header_tree.pack(fill="both", expand=True)

#     root.mainloop()

# if __name__ == "__main__":
#     main()
