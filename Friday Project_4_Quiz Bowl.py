import random

# Defining the questions
questions = {
    "What is the smallest planet in our solar system?": "Mercury",
    "Who developed the theory of relativity?": "Einstein",
    "Which country is the origin of the martial art 'Karate'?": "Japan",
    "What is the hardest natural substance on Earth?": "Diamond",
    "Who painted the 'Mona Lisa'?": "Leonardo da Vinci"
}

# Randomizing the questions
questions_list = list(questions.keys())  
random.shuffle(questions_list)  

# Asking the questions, checking the answers, and keeping score
correct_answers = 0

for question in questions_list:
    user_answer = input(question + " ")  
    if user_answer.lower() == questions[question].lower(): 
        print("Correct!")  
        correct_answers += 1  
    else:
        print(f"Wrong! The correct answer is {questions[question]}.")  

# Showing the final score
print(f"Your score is: {correct_answers}/{len(questions)}")
