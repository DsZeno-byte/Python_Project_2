# Python_Project_2

# Personal Diary Application

This is a simple personal diary application built using Python and Tkinter. The application allows users to write, save, and view their diary entries. The entries are saved in a text file along with a timestamp to track when each entry was created.

## Features

- **Write Diary Entries**: Users can write multi-line diary entries.
- **Save Entries**: Diary entries are saved in a text file with a timestamp for reference.
- **View Previous Entries**: Users can load and view all previously saved diary entries in a separate window.
- **Clear Text Area**: After saving, the text area is cleared, ready for a new entry.
- **Warning for Empty Entries**: A warning will be shown if the user tries to save an empty diary entry.
- **Exit Application**: Users can exit the application using the Exit button.

## Installation

1. **Install Python**: Ensure that you have Python 3.x installed on your machine.
   
   You can download Python from [python.org](https://www.python.org/).

2. **Install Tkinter**: Tkinter is included with Python, but in case it's not installed, you can install it using:
   
   ```bash
   pip install tk
3. Download the project files:
     Clone or download this repository to your local machine. 

    **Usage**

    **Running the Application** 
        1. Open a terminal or command prompt.  
        2. Navigate to the directory where the project is saved. 
        3. Run the Python script: 

            ```bash 
            python diary.py 
# Usage
- 1. **Writing an Entry:** When the application starts, you will see a text area where you can type your diary entry.. 
- 2. **Saving an Entry:** 
      - After writing your entry, click the Save Entry button to save your entry. 
      - A timestamp will be added, and the entry will be saved to the diary_entries.txt file. 
- 3. **Viewing Previous Entries:** Click the Load Previous Entries button to open a new window showing all previous diary entries. 
- 4. **Exiting the Application:** Click the Exit button to close the application.  
# Code Explanation 
- **save_entry()**: This function retrieves the text from the text area, adds a timestamp, and saves it to diary_entries.txt. If the text area is empty, it shows a warning message.

- **load_entries()**: This function opens diary_entries.txt and displays the saved entries in a new window. If the file does not exist, it shows an info message.

- **exit_app()**: This function closes the main application window.

- **Tkinter Widgets**: The application uses Tkinter widgets like Tk, Label, Text, Button, and Toplevel for the user interface.
