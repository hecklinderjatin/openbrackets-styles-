
import tkinter as tk

root=tk.Tk()
count=tk.IntVar()
lst=[]
def print_coloum():
      print(lst)

def helper():
         str=tk.StringVar()
       
         for i in range(count.get()):
             tk.Entry(root, textvariable=str).grid(row=0, column=i, sticky="w")
             lst.append(str.get())
         refelect= tk.Button(root, text="reflect", command=lambda:print_coloum)
         refelect.place()   

tk.Label(root, text="Number:-").grid(row=0, column=0, sticky='w')
x_entry = tk.Entry(root, textvariable=count).grid(row=0, column=1, sticky="w")

visible= tk.Button(root, text="visible", command=lambda:helper)
visible.grid(row=1, coloum=0) 



root.mainloop()