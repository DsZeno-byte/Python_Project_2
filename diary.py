import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime

# Function to save the diary entry to a file
def save_entry():
    # Get the text from the Text widget
    diary_text = text_area.get("1.0", tk.END).strip()
    
    # Check if there's text to save
    if diary_text == "":
        messagebox.showwarning("Warning", "Your diary entry is empty!")
        return
    
    # Get the current date and time
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    
    file_name = "diary_entries.txt"
    
    # Open the file in append mode to add new entries
    with open(file_name, "a") as file:
        file.write(f"{timestamp}\n{diary_text}\n\n")
    
    messagebox.showinfo("Success", "Diary entry saved successfully!")
    text_area.delete("1.0", tk.END)  # Clear the text area

# Function to load previous entries
def load_entries():
    if not os.path.exists("diary_entries.txt"):
        messagebox.showinfo("No Entries", "No saved diary entries found.")
        return
    
    with open("diary_entries.txt", "r") as file:
        entries = file.read()
    
    # Display the entries in a new window
    view_window = tk.Toplevel(root)
    view_window.title("Previous Entries")
    
    text_view = tk.Text(view_window, wrap=tk.WORD, width=50, height=20)
    text_view.pack(padx=10, pady=10)
    text_view.insert(tk.END, entries)
    text_view.config(state=tk.DISABLED)  # Make it read-only

# Function to exit the application
def exit_app():
    root.quit()

# Create the main application window
root = tk.Tk()
root.title("Personal Diary Application")

# Create a label for the title
label = tk.Label(root, text="Write Your Diary Entry", font=("Arial", 14))
label.pack(pady=10)

# Create a Text widget for multi-line input
text_area = tk.Text(root, wrap=tk.WORD, width=50, height=10)
text_area.pack(padx=10, pady=10)

# Create the buttons (Save, Load, Exit)
save_button = tk.Button(root, text="Save Entry", width=20, command=save_entry)
save_button.pack(pady=5)

load_button = tk.Button(root, text="Load Previous Entries", width=20, command=load_entries)
load_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", width=20, command=exit_app)
exit_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
