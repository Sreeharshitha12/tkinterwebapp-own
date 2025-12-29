"""
GUI DEVELOPMENT IN PYTHON USING TKINTER
====================================

THIS VERSION USES FULL SENTENCE-STYLE EXPLANATIONS.
Each method call is explained in 2–3 clear sentences so that
any beginner can understand WHAT the method does, WHY it is used,
and HOW it affects the GUI.
"""

# The tkinter module is imported and given the alias 'tk' so that
# all Tkinter classes and methods can be accessed easily using the tk prefix.
import tkinter as tk

# The ttk module is imported from tkinter to use modern themed widgets
# such as Combobox and Treeview, which provide a better look and feel.
from tkinter import ttk

# The messagebox module is imported to display dialog windows
# such as information messages, warnings, and error popups.
from tkinter import messagebox


# The Tk() method creates the main application window and initializes
# the Tkinter interpreter, which is required before creating any widgets.
root = tk.Tk()

# The title() method sets the text that appears in the title bar
# of the application window.
root.title("GUI Development in Python - Tkinter")

# The geometry() method sets the width and height of the window
# using pixel values in the format WIDTHxHEIGHT.
root.geometry("900x700")

# The iconbitmap() method sets a custom icon for the application window.
# The icon file must exist at the specified path, otherwise an error will occur.
root.iconbitmap("niralee.ico")


# This function is executed when the user clicks a button.
# It demonstrates event handling by responding to user interaction.
def on_button_click():
    # The showinfo() method displays a modal dialog box with a title
    # and a message to inform the user about an event.
    messagebox.showinfo("Event Triggered", "Button Clicked Successfully!")


# This function is used to close the application safely.
# It stops the Tkinter event loop and exits the program.
def exit_app():
    root.quit()


# The Menu() method creates a menu bar object that can hold
# multiple drop-down menus such as File and Help.
menu_bar = tk.Menu(root)

# A File menu is created using the Menu() method.
# The tearoff=0 option removes the dashed line at the top of the menu.
file_menu = tk.Menu(menu_bar, tearoff=0)

# The add_command() method adds a clickable menu item to the File menu.
# When clicked, it executes the exit_app() function.
file_menu.add_command(label="Exit", command=exit_app)

# The add_cascade() method attaches the File menu to the menu bar
# under the label "File".
menu_bar.add_cascade(label="File", menu=file_menu)

# A Help menu is created to provide additional information to the user.
help_menu = tk.Menu(menu_bar, tearoff=0)

# The add_command() method adds an About option to the Help menu.
# A lambda function is used to display a messagebox when clicked.
help_menu.add_command(
    label="About",
    command=lambda: messagebox.showinfo("About", "Tkinter GUI Demo")
)

# The Help menu is attached to the menu bar using add_cascade().
menu_bar.add_cascade(label="Help", menu=help_menu)

# The config() method is used to attach the menu bar to the root window
# so that it appears at the top of the application.
root.config(menu=menu_bar)


# A Frame widget is created to act as a toolbar container.
# Background color, border width, and relief style are used for visual effect.
toolbar = tk.Frame(root, bg="lightgray", relief=tk.RAISED, bd=2)
# A Button widget is created inside the toolbar.
# The command parameter links the button click to a function.
btn_toolbar = tk.Button(toolbar, text="Click Me", command=on_button_click)
# The pack() method places the button inside the toolbar.
# side=tk.LEFT aligns the button to the left and padx adds spacing.
btn_toolbar.pack(side=tk.LEFT, padx=2)
# The toolbar is placed at the top of the window.
# The fill=tk.X option stretches it horizontally across the window.
toolbar.pack(side=tk.TOP, fill=tk.X)
# A StringVar object is created to store and update text dynamically.
# It is commonly used with Labels, Entries, and Status Bars.
status_var = tk.StringVar()
# The set() method assigns an initial value to the StringVar.
status_var.set("Ready")
# A Label widget is created to act as a status bar at the bottom of the window.
# The textvariable option links the label to the StringVar object.
status_bar = tk.Label(root, textvariable=status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
# The pack() method places the status bar at the bottom of the window.
# The fill=tk.X option makes it stretch horizontally.
status_bar.pack(side=tk.BOTTOM, fill=tk.X)
# A Frame widget is created to group form-related widgets together.
main_frame = tk.Frame(root)
# The pack() method places the frame in the window with vertical spacing.
main_frame.pack(pady=10)
# A Label widget is created to display a descriptive text for the input field.
label = tk.Label(main_frame, text="Enter Your Name:")
# The grid() method places the label in the first row and first column
# and adds spacing around it using padx and pady.
label.grid(row=0, column=0, padx=5, pady=5)
# An Entry widget is created to allow the user to enter text input.
entry = tk.Entry(main_frame)
# The grid() method places the entry field next to the label.
entry.grid(row=0, column=1, padx=5, pady=5)
# A Button widget is created to submit the entered data.
button = tk.Button(main_frame, text="Submit", command=on_button_click)
# The grid() method places the submit button next to the entry field.
button.grid(row=0, column=2, padx=5, pady=5)
# A Scale widget is created to allow the user to select a numeric value.
# The slider ranges from 0 to 100 and is displayed horizontally.
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Volume")
# The pack() method places the Scale widget in the window.
# The pady parameter adds vertical spacing for better layout appearance.
scale.pack(pady=10)
# A Spinbox widget is created to allow numeric selection using arrow buttons.
# The values range from 1 to 10.
spinbox = tk.Spinbox(root, from_=1, to=10)
# The pack() method places the Spinbox widget below the Scale widget.
spinbox.pack(pady=10)
# A Listbox widget is created to display a list of selectable items.
listbox = tk.Listbox(root, height=4)
# The insert() method adds programming language names to the Listbox.
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
# The pack() method places the Listbox widget in the window.
listbox.pack(pady=10)
# A Combobox widget is created to provide a drop-down list of countries.
combo = ttk.Combobox(root, values=["India", "USA", "UK", "Canada"])
# The set() method assigns a default display text to the Combobox.
combo.set("Select Country")
# The pack() method places the Combobox widget in the window.
combo.pack(pady=10)
# Column names are defined for displaying tabular data in the Treeview widget.
columns = ("ID", "Name", "Course")
# A Treeview widget is created to display data in table format.
# The show="headings" option hides the default empty column.
tree = ttk.Treeview(root, columns=columns, show="headings")
# The heading() method defines the column headers for the table.
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Course", text="Course")
# The insert() method adds rows of data to the Treeview widget.
tree.insert("", tk.END, values=(1, "Nischal", "Python"))
tree.insert("", tk.END, values=(2, "Alex", "Java"))
# The pack() method places the Treeview widget in the window.
tree.pack(pady=10)
# A Canvas widget is created to draw graphics such as lines and shapes.
canvas = tk.Canvas(root, width=300, height=200, bg="white")
# The create_line() method draws a straight blue line on the canvas.
canvas.create_line(10, 10, 200, 10, fill="blue", width=2)
# The create_rectangle() method draws a red rectangular box on the canvas.
canvas.create_rectangle(50, 50, 150, 120, outline="red", width=2)
# The pack() method places the Canvas widget in the window.
canvas.pack(pady=10)
# The mainloop() method starts the Tkinter event loop.
# It keeps the window open and continuously listens for user interactions.
root.mainloop()
