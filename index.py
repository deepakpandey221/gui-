import tkinter as tk
from tkinter import messagebox, simpledialog

def login():
    password = simpledialog.askstring("Password", "Enter your password:", show="*")
    if password == "12345":
        window.destroy()
        open_new_page()
    else:
        messagebox.showwarning("Login Failed", "Invalid password!")

def open_new_page():
    # Create a new window
    new_window = tk.Tk()
    new_window.title("New Page")

    # Set the window size to match the screen size
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()
    new_window.geometry(f"{screen_width}x{screen_height}")

    # Load the background image
    background_image = tk.PhotoImage(file="ddp.png")

    # Create a label widget to hold the background image
    background_label = tk.Label(new_window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Customize button names
    button_names = ["Check Cal", "See Date", "Make Directory", "Create File", "Create a User", "Delete a User", "Change password of a user", "Configure Web Server", "Button I", "Exit"]

    # Create ten  buttons
    buttons = []
    for i in range(10):
        button = tk.Button(new_window, text=button_names[i], font=("Arial", 24), width=21, height=2)
        buttons.append(button)

    for i, button in enumerate(buttons):
        button.grid(row=i // 2, column=i % 2, padx=5, pady=5)
    new_window.mainloop()

# Create the main window
window = tk.Tk()

# Load the background image
background_image = tk.PhotoImage(file="ddp.png")

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Create a label widget to hold the background image
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, width=screen_width, height=screen_height)

# Create a label for the text
text_label = tk.Label(window, text="Welcome to the Login Page", font=("Arial", 18), fg="black")
text_label.place(relx=0.5, rely=0.4, anchor="center")

# Create a button widget
login_button = tk.Button(window, text="Login", command=login)

# Set the coordinates for the login button
button_x = 750
button_y = 400

# Place the button at the specified coordinates
login_button.place(x=button_x, y=button_y)

# Start the main event loop
window.mainloop()
