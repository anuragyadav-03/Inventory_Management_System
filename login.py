import tkinter as tk
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import os

def login():
    username = username_entry.get()
    password = password_entry.get()

    conn = mysql.connector.connect(host='localhost', database='inventory_system', user='root', password='')
    c = conn.cursor()

    c.execute('SELECT * FROM test WHERE username=%s AND password=%s', (username, password))
    user = c.fetchone()

    if user is not None:
        # switch to main page here
        main_page()
    else:
        login_error_label = tk.Label(login_frame, text="Invalid username or password", font=("Arial", 16), bg="#f2f2f2", fg="#f00")
        login_error_label.pack(pady=10)

    conn.close()

def main_page():
    os.system('python D:\\Anurag-PC\\OneDrive\\Desktop\\Inventory-Management\\main.py')
    root.destroy()

def register():
    # Retrieve the entered details
    full_name = full_name_entry.get()
    email = email_entry.get()
    username = register_username_entry.get()
    password = register_password_entry.get()
    confirm_password = confirm_password_entry.get()
    
	# Check if the password and confirm password match
    if password != confirm_password:
        register_error_label = tk.Label(register_frame, text="Passwords do not match", font=("Arial", 16), bg="#f2f2f2", fg="#f00")
        register_error_label.pack(pady=10)
        return
    
    conn = mysql.connector.connect(host='localhost',
                                       database='inventory_system',
                                       user='root',
                                       password='')
    
    # Insert the user details into the database
    c = conn.cursor()

    c.execute("INSERT INTO test (full_name, email, username, password) VALUES (%s, %s, %s, %s)", (full_name, email, username, password))
    conn.commit()
    
    register_success_label = tk.Label(register_frame, text="Registration successful!", font=("Arial", 16), bg="#f2f2f2", fg="#0f0")
    register_success_label.pack(pady=10)

    conn.close()

root = tk.Tk()
root.title('Login')



# Create a Notebook widget that will hold two tabs: Login and Register
notebook = ttk.Notebook(root, width=1366, height=768)
notebook.pack(pady=50)

# Create the Login tab
login_frame = tk.Frame(notebook, width=1366, height=768, bg="#f2f2f2")
login_frame.pack(fill="both", expand=True)
notebook.add(login_frame, text="Login")

# Add widgets to the Login tab
login_label = tk.Label(login_frame, text="Login", font=("Arial", 24), bg="#f2f2f2")
login_label.pack(pady=50)

username_label = tk.Label(login_frame, text="Username:", font=("Arial", 16), bg="#f2f2f2")
username_label.pack(pady=10)

username_entry = tk.Entry(login_frame, font=("Arial", 16))
username_entry.pack()

password_label = tk.Label(login_frame, text="Password:", font=("Arial", 16), bg="#f2f2f2")
password_label.pack(pady=10)

password_entry = tk.Entry(login_frame, show="*", font=("Arial", 16))
password_entry.pack()

login_button = tk.Button(login_frame, text="Login", font=("Arial", 16), bg="green", fg="#fff", command=login)
login_button.pack(pady=20)

error_label = tk.Label(root, fg='red')
error_label.pack()

# Create the Register tab
register_frame = tk.Frame(notebook, width=1366, height=768, bg="#f2f2f2")
register_frame.pack(fill="both", expand=True)
notebook.add(register_frame, text="Register")

# Add widgets to the Register tab
register_label = tk.Label(register_frame, text="Register", font=("Arial", 24), bg="#f2f2f2")
register_label.pack(pady=50)

full_name_label = tk.Label(register_frame, text="Full Name:", font=("Arial", 16), bg="#f2f2f2")
full_name_label.pack(pady=10)

full_name_entry = tk.Entry(register_frame, font=("Arial", 16))
full_name_entry.pack()

email_label = tk.Label(register_frame, text="Email:", font=("Arial", 16), bg="#f2f2f2")
email_label.pack(pady=10)

email_entry = tk.Entry(register_frame, font=("Arial", 16))
email_entry.pack()

register_username_label = tk.Label(register_frame, text="Username:", font=("Arial", 16), bg="#f2f2f2")
register_username_label.pack(pady=10)

register_username_entry = tk.Entry(register_frame, font=("Arial", 16))
register_username_entry.pack()

register_password_label = tk.Label(register_frame, text="Password:", font=("Arial", 16), bg="#f2f2f2")
register_password_label.pack(pady=10)

register_password_entry = tk.Entry(register_frame, show="*", font=("Arial", 16))
register_password_entry.pack()

confirm_password_label = tk.Label(register_frame, text="Confirm Password:", font=("Arial", 16), bg="#f2f2f2")
confirm_password_label.pack(pady=10)

confirm_password_entry = tk.Entry(register_frame, show="*", font=("Arial", 16))
confirm_password_entry.pack()

register_button = tk.Button(register_frame, text="Register", font=("Arial", 16), bg="steelblue", fg="#fff", command=register)
register_button.pack(pady=20)

success_label = tk.Label(root, fg='green')
success_label.pack()

root.geometry("1366x785+0+0")
root.title("Security Page !!")
root.mainloop()