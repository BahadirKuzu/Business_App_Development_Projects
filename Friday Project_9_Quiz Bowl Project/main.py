import tkinter as tk
from tkinter import messagebox
import sqlite3
import random

# Main window for category selection
def main_window():
    root = tk.Tk()
    root.title("Quiz")
    root.geometry("300x250")

    # Adding padding and title for a neat layout
    tk.Label(root, text="Select your category", font=("Arial", 12)).pack(pady=(20, 5))
    category_var = tk.StringVar()
    category_var.set("Countries")

    # Categories for the quiz
    categories = ["Countries", "Sports", "Movies", "Travel", "Nature"]
    for category in categories:
        tk.Radiobutton(root, text=category, variable=category_var, value=category, font=("Arial", 10)).pack(anchor='w', padx=20)

    # Start Quiz button with minimal bottom padding
    tk.Button(root, text="Start Quiz", command=lambda: start_quiz(category_var.get(), root), font=("Arial", 10)).pack(pady=(10, 2))
    root.mainloop()

# Function to start the quiz with the selected category
def start_quiz(category, main_window):
    # Close the main window
    main_window.destroy()
    # Create quiz window
    quiz_win = tk.Tk()
    quiz_win.title(f"{category} Quiz")
    quiz_win.geometry("440x230")

    try:
        # Connect to the database and get questions for the selected category
        conn = sqlite3.connect('questions.db')
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {category}')
        questions = cursor.fetchall()
        
        # Select exactly 10 unique questions without duplication
        questions = random.sample(questions, min(10, len(questions)))

        # If questions exist in the category, start displaying them
        if questions:
            QuestionDisplay(quiz_win, questions).display_question(0)
        else:
            messagebox.showwarning("No Questions", "No questions available in this category.")
            quiz_win.destroy()

    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
        quiz_win.destroy()
    finally:
        conn.close()

# Class to handle question display and answer submission
class QuestionDisplay:
    def __init__(self, parent, questions):
        self.parent = parent
        self.questions = questions
        self.score = 0
        self.answer_var = tk.StringVar()
        self.current_index = 0  # To track the current question index

    # Display each question
    def display_question(self, question_index):
        if question_index < len(self.questions):
            question_data = self.questions[question_index]
            question_text = question_data[1]
            options = [question_data[2], question_data[3], question_data[4], question_data[5]]
            correct_answer = question_data[6]

            # Clear previous widgets
            for widget in self.parent.winfo_children():
                widget.destroy()

            # Display question number and text with padding
            tk.Label(self.parent, text=f"{question_index + 1}. {question_text}", font=("Arial", 12), wraplength=420).pack(pady=(25, 5))
            self.answer_var.set(None)

            # Display options as radio buttons with labeled choices (A, B, C, D)
            option_labels = ["A) ", "B) ", "C) ", "D) "]
            for i, option in enumerate(options):
                option_text = option_labels[i] + option if not option.startswith(option_labels[i]) else option
                tk.Radiobutton(self.parent, text=option_text, variable=self.answer_var, value=option, font=("Arial", 10)).pack(anchor='w', padx=25)

            # Submit button with controlled padding
            submit_button = tk.Button(self.parent, text="Submit Answer", 
                                      command=lambda: self.check_answer(correct_answer, question_index), font=("Arial", 10))
            submit_button.pack(pady=(10, 20))

    # Check if the answer is correct
    def check_answer(self, correct_answer, question_index):
        # Remove the label from both correct answer and selected answer for accurate comparison
        selected_answer = self.answer_var.get()
        stripped_correct_answer = correct_answer.split(" ", 1)[-1]  # Strip "A) ", "B) ", etc.
        stripped_selected_answer = selected_answer.split(" ", 1)[-1]  # Strip "A) ", "B) ", etc.

        if stripped_selected_answer == stripped_correct_answer:
            messagebox.showinfo("Result", "Correct Answer!")
            self.score += 1
        else:
            messagebox.showinfo("Result", "Incorrect!")

        # Move to the next question or show final score
        next_question_index = question_index + 1
        if next_question_index < len(self.questions):
            self.display_question(next_question_index)
        else:
            messagebox.showinfo("Quiz Complete", f"Your score is {self.score} out of {len(self.questions)}")
            self.parent.destroy()

# Run the main window
main_window()
