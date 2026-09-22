Python Console Quiz Game
A simple, interactive command-line quiz application built with Python. The game asks a series of general knowledge and basic programming questions, validates user answers case-insensitively, tracks the score, and provides performance feedback at the end.

Features
Interactive CLI Interface: Prompts the user question-by-question directly in the terminal.

Case-Insensitive Answer Checking: Converts inputs to lowercase so variations in capitalization are accepted.

Instant Feedback: Alerts the player immediately if an answer is correct or reveals the correct answer upon an incorrect guess.

Dynamic Scoring & Rating: Calculates the final score against total questions and displays a tailored performance message.

Code Breakdown
1. Score Tracking & State Initialization
Python
score = 0
A counter variable named score is initialized to 0 to keep track of the number of correct responses.

2. Question–Answer Data Structure
Python
questions = [
    ["What is the capital of Pakistan?", "Islamabad"],
    ["Which language are we using?", "Python"],
    ["What is 5 + 5?", "10"],
    ["Which keyword is used to create a function?", "def"],
    ["What type of data is 10?", "int"]
]
The quiz content is stored in a 2D list (a list of lists). Each sub-list contains two elements:

Index 0: The question prompt.

Index 1: The expected answer string.

3. Iteration and Input Validation
Python
for question in questions:
    answer = input("\n" + question[0] + " ")

    if answer.lower() == question[1].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer:", question[1])
A for loop iterates through each sub-list in questions.

input() displays the prompt and halts execution until the player enters their response.

The .lower() string method normalizes both the user's input and the stored answer to lowercase, preventing unintended rejections due to letter case mismatches (e.g., Islamabad vs. islamabad).

If matched, score increments by 1; otherwise, the correct answer is printed to the console.

4. Results Evaluation & Feedback
Python
print("\n==============================")
print("Quiz Finished!")
print("Your score:", score, "/", len(questions))
print("==============================")

if score == len(questions):
    print("Excellent!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practicing!")
len(questions) dynamically retrieves the total question count (5 in this case).

An if-elif-else conditional evaluates the final score and prints a corresponding rating:

Full score: Excellent!

3 or more correct: Good job!

Fewer than 3 correct: Keep practicing!