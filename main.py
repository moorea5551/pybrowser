import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Waterturtle - A browser that's basically the opposite of Firefox")
root.minsize(800, 500)

url = "myurl"
urlBarFrame = ttk.Frame(root).pack()
urlBar = ttk.Entry(urlBarFrame, width=15, textvariable=url)
urlBar.grid(column=0, row=0)

root.mainloop()