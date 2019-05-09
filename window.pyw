from tkinter import messagebox
import tkinter as tk

def hehelix():
	hehelixgif=tk.Label(window, image=pic)
	hehelixgif.pack()
	
def function():
	messagebox.showerror("hehelix","shut up retard")

def both():
	function()
	hehelix()

window=tk.Tk()
window.title("window")
window.geometry("1200x800")

root_menu = tk.Menu(window)
window.config(menu = root_menu)

file_menu = tk.Menu(root_menu)
root_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New file.....", command = function)
file_menu.add_command(label = "Open files", command = function)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = window.quit)

edit_menu = tk.Menu(root_menu)
root_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Undo", command = function)
edit_menu.add_command(label = "Redo", command = function)

top_frame = tk.Frame(window).pack()
bottom_frame = tk.Frame(window).pack(side = "bottom")

tk.Label(window,text="hieeee").pack()
tk.Button(top_frame,text="hehelix!",fg="black",command=both).pack()

pic=tk.PhotoImage(file="HEHELIX.gif")

window.mainloop()