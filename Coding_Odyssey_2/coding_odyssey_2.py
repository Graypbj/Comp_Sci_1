import tkinter as tk
from tkinter import ttk


def save_note():
    selected_tab = notebook.index(notebook.select())
    note = text.get("1.0", "end-1c")
    file_name = f"note_{selected_tab}.txt"
    with open(file_name, "w") as file:  # Use "w" to write the note (overwriting the existing content)
        file.write(note)
    text.delete("1.0", "end")


def clear_note():
    text.delete("1.0", "end")


# Create a main window
window = tk.Tk()
window.title("Note Taking App")

# Create a notebook for tabs
notebook = ttk.Notebook(window)
notebook.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)


# Function to create a new tab
def create_tab():
    tab = tk.Frame(notebook)
    notebook.add(tab, text=f"Tab {notebook.index(notebook.select()) + 1}")
    create_text_area(tab)


# Function to create a text area within a tab
def create_text_area(tab):
    text_frame = tk.Frame(tab)
    text_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    text = tk.Text(text_frame, wrap=tk.WORD)
    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(text_frame, command=text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text.config(yscrollcommand=scrollbar.set)


# Button to create a new tab
add_tab_button = tk.Button(window, text="Create Tab", command=create_tab)
add_tab_button.pack(side=tk.TOP, padx=10, pady=10)

# Create initial tab
create_tab()

# Create "Save" and "Clear" buttons
save_button = tk.Button(window, text="Save", command=save_note)
clear_button = tk.Button(window, text="Clear", command=clear_note)
save_button.pack(side=tk.LEFT, padx=10, pady=10)
clear_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Start the GUI main loop
window.mainloop()
