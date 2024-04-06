import tkinter as tk

def run_gui():
    root = tk.Tk()
    root.geometry("800x600")

    frame2 = tk.Frame(root, bg='white', highlightthickness=1, highlightbackground="black")
    frame2.pack(fill=tk.BOTH, expand=True)

    frame3 = tk.Frame(root, bg='white', highlightthickness=1, highlightbackground="black")
    frame3.pack(fill=tk.BOTH, expand=True)

    def on_drag_start(event):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y

    def on_drag_motion(event):
        widget = event.widget
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        widget.place(x=x, y=y)

    def on_drag_end(event):
        pass

    def add_button():
        new_button = tk.Button(frame2, text="Dynamic Button")
        new_button.bind("<ButtonPress-1>", on_drag_start)
        new_button.bind("<B1-Motion>", on_drag_motion)
        new_button.bind("<ButtonRelease-1>", on_drag_end)
        new_button.pack()

    def add_label():
        new_label = tk.Label(frame2, text="Dynamic Label")
        new_label.bind("<ButtonPress-1>", on_drag_start)
        new_label.bind("<B1-Motion>", on_drag_motion)
        new_label.bind("<ButtonRelease-1>", on_drag_end)
        new_label.pack()

    button_add_button = tk.Button(frame3, text="Add Button", command=add_button)
    button_add_button.pack()

    button_add_label = tk.Button(frame3, text="Add Label", command=add_label)
    button_add_label.pack()

    root.mainloop()

run_gui()
