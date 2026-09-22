print("==============================")
print("        PYTHON QUIZ")
print("==============================")

score = 0

questions = [
    ["What is the capital of Pakistan?", "Islamabad"],
    ["Which language are we using?", "Python"],
    ["What is 5 + 5?", "10"],
    ["Which keyword is used to create a function?", "def"],
    ["What type of data is 10?", "int"]
]

for question in questions:

    answer = input("\n" + question[0] + " ")

    if answer.lower() == question[1].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer:", question[1])

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