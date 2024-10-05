def trivia_quiz():
    questions = {
        "What is the capital of France?": {
            "options": ["A) London", "B) Paris", "C) Rome", "D) Berlin"],
            "answer": "B"
        },
        "Which planet is known as the Red Planet?": {
            "options": ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"],
            "answer": "C"
        },
        "What is the largest mammal in the world?": {
            "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Great White Shark"],
            "answer": "B"
        },
        "Which element has the chemical symbol 'O'?": {
            "options": ["A) Gold", "B) Oxygen", "C) Silver", "D) Helium"],
            "answer": "B"
        },
        "What year did the Titanic sink?": {
            "options": ["A) 1905", "B) 1912", "C) 1918", "D) 1925"],
            "answer": "B"
        }
    }

    score = 0

    print("Welcome to the Trivia Quiz!")
    print("Answer the following questions:\n")

    for question, data in questions.items():
        print(question)
        for option in data["options"]:
            print(option)
        player_answer = input("Your answer (A/B/C/D): ").upper()

        if player_answer == data["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {data['answer']}.\n")

    print(f"You finished the quiz! Your score: {score}/{len(questions)}")

# Start the game
trivia_quiz()
