import random
def ask_question():
    questions = {
        "What is the capital of France?": "Paris",
        "What is the largest planet in our solar system?": "Jupiter",
        "Who wrote 'Harry Potter'?": "J.K. Rowling",
        "What is the smallest prime number?": "2",
        "What is the chemical symbol for water?": "H2O",
        "37 % 3 = ?": "1"
    }
    
    question, correct_answer = random.choice(list(questions.items()))

    user_answer = input(f"{question}\nYour Answer: ").capitalize()

    if user_answer == correct_answer.capitalize():
        print("Correct Answer! 🎉")
        return 5
    else:
        print(f"Wrong Answer! The correct answer is {correct_answer}.")
        return 0

print("Welcome to the Quiz")
playing = input("Do you want to play?...Y/N\n").lower()

if playing == "n":
    print("Exiting the game. Goodbye!")
    quit()
elif playing == "y":
    print("\nLet's Play!! :-)")
    print("Each correct answer will score 5 points, and incorrect answers score 0 points.\n")

    score = 0
    while True:
        print("Enter 1 for a new question and 0 to exit")
        z = int(input())
        
        if z == 0:
            print(f"Exiting the game. Final Score: {score}. Goodbye!")
            quit()
        elif z == 1:
            score += ask_question()
            print(f"Current Score: {score}\n")
        else:
            print("Invalid input! Please enter 1 for a new question or 0 to exit.\n")
