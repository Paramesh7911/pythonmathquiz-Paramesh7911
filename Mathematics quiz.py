# THANOSNAPP Mathematics Quiz

def mathematics_quiz():
    print("Welcome to THANOSNAPP Mathematics Quiz!")
    score = 0

    questions = [
        {
            "question": "1. What is 7 + 8?",
            "options": ["A) 14", "B) 15", "C) 16", "D) 17"],
            "answer": "B"
        },
        {
            "question": "2. What is the square root of 64?",
            "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
            "answer": "C"
        },
        {
            "question": "3. Solve: 5 * 6 - 4 + 3",
            "options": ["A) 28", "B) 29", "C) 30", "D) 31"],
            "answer": "B"
        },
        {
            "question": "4. What is the value of pi (π) approximately?",
            "options": ["A) 3.12", "B) 3.14", "C) 3.16", "D) 3.18"],
            "answer": "B"
        },
        {
            "question": "5. If 4x = 20, what is x?",
            "options": ["A) 4", "B) 5", "C) 6", "D) 7"],
            "answer": "B"
        }
    ]

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")

    print(f"\nQuiz completed! Your total score is: {score}/5")

mathematics_quiz()
