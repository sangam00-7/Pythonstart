# python quiz game

questions = (
    "How many elements are in the periodic table?",
    "Which is the largest country in the world?",
    "Which is the longest river in the world?",
    "Which is the largest forest in the world?",
    "How many oceans are there in total?"
)

options = (
    ("A. 116", "B. 115", "C. 114", "D. 118"),
    ("A. India", "B. China", "C. America", "D. Russia"),
    ("A. Karnali", "B. Nile", "C. Amazon", "D. Mississippi"),
    ("A. Amazon", "B. Congo", "C. Black Forest", "D. Great Bear"),
    ("A. 2", "B. 4", "C. 5", "D. 6")
)

answers = ("D", "D", "B", "A", "C")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"\nYour score is: {score}%")