def quiz_app():
    # Dictionary to store questions and answers
    questions = {
        "What is the capital of France? ": "Paris",
        "Who wrote 'To Kill a Mockingbird'? ": "Harper Lee",
        "What is 5 + 7? ": "12",
        "Which planet is known as the Red Planet? ": "Mars",
        "What is the boiling point of water in Celsius? ": "100"
    }
    
    score = 0  # To track the user's score

    print("Welcome to the Quiz! Answer the following questions:\n")

    # Loop through each question
    for question, correct_answer in questions.items():
        user_answer = input(question).strip()

        # Check if the answer is correct
        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}\n")
    
    # Display the final score
    print(f"Quiz Over! Your total score is: {score}/{len(questions)}")

# Run the quiz
quiz_app()
