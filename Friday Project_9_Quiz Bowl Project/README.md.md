# QuizBowlProject


## Overview
This project is a Quiz application where users can take quizzes across different categories. The questions are stored in a SQLite database, and a graphical user interface (GUI) is provided for user interaction.

## File Structure
- `addDataToDB.py`: This file contains the code to create the SQLite database and populate it with questions for various categories.
- `main.py`: This is the main application file that creates the GUI for the quiz and handles user interactions.
- `questions.db`: The SQLite database file that stores questions categorized into different subjects.
- `readDB.py`: This file reads from the SQLite database and displays the questions and answers for each category.
- `README.md`: Documentation for the project.

## Setup Instructions
1. **Install Dependencies**: Ensure you have Python installed along with the `sqlite3` and `tkinter` libraries. These libraries come with Python by default.
   
2. **Create the Database**:
   - Run the `addDataToDB.py` file to create the `questions.db` database and populate it with questions.

   ```bash
   python addDataToDB.py
   ```

3. **Start the Quiz Application**:
   - To start the quiz application, run the `main.py` file.

   ```bash
   python main.py
   ```

4. **Reading Data from the Database**:
   - If you want to view the questions and the categories in the database, you can run the `readDB.py` file.

   ```bash
   python readDB.py
   ```

## Usage
- Launch the application by running `main.py`. You will see a window where you can select a quiz category.
- Choose a category (e.g., Countries, Sports, Movies, Travel, Nature) and click on "Start Quiz".
- Answer the questions presented, and at the end of the quiz, you will receive your score.

## Features
- Multiple choice questions across various categories.
- A user-friendly GUI to facilitate quiz taking.
- Random selection of questions to enhance the quiz experience.
- Feedback provided for each answer submitted.

## Author
- Bahadir Kuzu

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
