import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog

# Database Setup
def setup_database():
    conn = sqlite3.connect('customer_feedback.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        feedback TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Function to submit feedback to the database
def submit_feedback():
    name = entry_name.get()
    email = entry_email.get()
    feedback = entry_feedback.get("1.0", tk.END).strip()

    if name and email and feedback:
        conn = sqlite3.connect('customer_feedback.db')
        c = conn.cursor()
        c.execute("INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)", (name, email, feedback))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Feedback submitted successfully!")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_feedback.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

# Function to retrieve data with password protection
def retrieve_data():
    password = "123"  # Set your password here
    entered_password = simpledialog.askstring("Password", "Enter the password to retrieve feedback:", show='*')

    if entered_password == password:
        conn = sqlite3.connect('customer_feedback.db')
        c = conn.cursor()
        c.execute("SELECT name, email, feedback FROM feedback")
        feedback_entries = c.fetchall()
        conn.close()

        if feedback_entries:
            print("\nFeedback Entries:")
            for entry in feedback_entries:
                print(f"Name: {entry[0]}, Email: {entry[1]}, Feedback: {entry[2]}")
        else:
            print("No feedback entries found.")
    else:
        messagebox.showerror("Access Denied", "Incorrect password.")

# Initialize main application window
app = tk.Tk()
app.title("Customer Feedback")

# Create input fields and labels
tk.Label(app, text="Name").pack()
entry_name = tk.Entry(app)
entry_name.pack()

tk.Label(app, text="Email").pack()
entry_email = tk.Entry(app)
entry_email.pack()

tk.Label(app, text="Feedback").pack()
entry_feedback = tk.Text(app, height=5, width=30)
entry_feedback.pack()

# Submit button
btn_submit = tk.Button(app, text="Submit", command=submit_feedback)
btn_submit.pack()

# Retrieve Data button
btn_retrieve = tk.Button(app, text="Retrieve Data", command=retrieve_data)
btn_retrieve.pack()

# Run the setup database function
setup_database()

# Run the Tkinter event loop
app.mainloop()
