<<<<<<< HEAD
# Friday Project 8: Customer Feedback Application

This is a simple Python application that allows customers to submit feedback through a graphical user interface (GUI). The feedback data, including the customer's name, email, and message, is stored in an SQLite database. Additionally, the application includes a password-protected feature to retrieve all feedback entries in the console.

## Features

- **Submit Feedback**: Customers can enter their name, email, and feedback message into the GUI. This data is then stored securely in an SQLite database.
- **Retrieve Feedback**: An option to retrieve and view all feedback entries with password protection ensures that only authorized users can access this data.

## Technologies Used

- **Python**: Programming language used for application development.
- **SQLite**: Lightweight database for storing feedback data.
- **Tkinter**: GUI library for creating the user interface.

## Requirements

- Python 3.x
- SQLite (included with Python’s standard library)
- Tkinter (comes with Python on most platforms)

## Installation

1. Download the project files or clone this repository.
2. Ensure you have Python 3.x installed on your system.

## How to Run

1. Open a terminal or command prompt in the project directory.
2. Run the following command to start the application:

   ```bash
   python customer_feedback_app.py
3. The application window will open, allowing users to submit feedback.

## Usage

### Submitting Feedback
1. In the application window, enter your **Name**, **Email**, and **Feedback Message**.
2. Click the **"Submit"** button to store the feedback in the database.
3. A confirmation message will appear once the feedback is successfully submitted.

### Retrieving Feedback
1. Click the **"Retrieve Data"** button in the application.
2. A password prompt will appear. Enter the password (default is `123`) to access feedback entries.
3. If the correct password is entered, all feedback entries will display in the console.
4. If the password is incorrect, an error message will appear, and access to feedback entries will be denied.

## Security Notes

- The password for retrieving feedback is currently set to `123` in the code. You can update this password by modifying the code if needed.
- For enhanced security in a production environment, consider implementing additional security measures, such as password hashing or encrypting the feedback data.

## Troubleshooting

- **Feedback entries not displayed when retrieving data**:
  - Ensure you have entered the correct password.
  - Confirm that there are feedback entries stored in the database.

- **Application not launching**:
  - Make sure you are running Python 3.x.
  - Verify that all necessary files are in the project directory and that `customer_feedback_app.py` is executed from this location.

## License

This project is licensed under the MIT License.
=======
# Friday-Project-8-Customer-Feedback
>>>>>>> 0456c2753359079c4a5510217f3e180cee7b193b
