import random

def calculator():
    print("Welcome to the Calculator!")
    while True:
        expression = input("Enter an expression to evaluate (or type 'exit' to quit): ")
        if expression.lower() == 'exit':
            break
        try:
            result = eval(expression)
            print(f"Result: {result}")
        except Exception as e:
            print("Invalid input. Please try again.")


def coding_problem():
    print("Welcome to the Coding Problem!")
    problem = "Write a Python function to calculate the factorial of a number."
    solution = """
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
"""
    print(f"Problem: {problem}")
    print("Solution:")
    print(solution)


def maths_quiz():
    print("Let's play a maths quiz")
    print("Are you ready?")
    print("Please select the difficulty level:")
    print("Easy(1), Medium(2), Hard(3)")
    difficulty = int(input("Enter your option (1/2/3): "))
    maths_que = {
        "30-54+64": "40",
        "(65-33)/32": "1",
        "(20-4-16)*56": "0",
        "(67-33)*0": "0",
    }
    random_que = random.choice(list(maths_que.keys()))
    print(f"Here's your question: {random_que}")
    ans = input("Enter your answer: ")
    correct_ans = maths_que[random_que]
    if ans == correct_ans:
        print("Correct answer!")
    else:
        print("Sorry, wrong answer.")


def games():
    while True:
        print("\nGaming section please select the game which you want to play")
        print("1. Guess the Number")
        print("2. Hangman")
        print("3. Rock, Paper, Scissors")
        print("4. Tic Tac Toe")

        choice = input("Choose an option(1, 2, 3, 4, ): ")

        if choice == '1':
            guess_the_number()
        elif choice == '2':
            guess_the_number()
            # hangman()
        elif choice == '3':
            rock_paper_scissors()
        elif choice == '4':
            guess_the_number()
            # tic_tac_toe()

        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def guess_the_number():
    print("Welcome to Guess the Number!")
    number = random.randint(1, 50)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 50: "))
            attempts += 1
            if guess > number:
                print("Lower!")
            elif guess < number:
                print("Higher!")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")


def rock_paper_scissors():
    print("Welcome to rock, paper, scissors!")
    print("Its between between you and the computer!")
    while True:
        try:
            computer_choice = random.choice(["rock", "paper", "scissors"])
            your_dict = {"rock": 1, "paper": 2, "scissors": 3}
        
            your_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
            if your_choice not in your_dict:
                print("Invalid choice. Please choose rock, paper, or scissors.")
            else:
                you = your_dict[your_choice]
                computer = your_dict[computer_choice]

                if computer == you:
                    result = "Draw"
                elif (computer == 1 and you == 2) or (computer == 2 and you == 3) or (computer == 3 and you == 1):
                    result = "You win!"
                else:
                    result = "You lose"

                print(f"Computer chose: {computer_choice.capitalize()}")
                print(result)
        finally:
            print("Thanks for playing!")


def main():
    while True:
        print("\nPython Mobile Menu:")
        print("1. Calculator")
        print("2. Coding Problem")
        print("3. Maths Quiz")
        print("4. Games")
        print("5. Exit")
        choice = input("Choose an option(1, 2, 3, 4, 5): ")

        if choice == '1':
            calculator()
        elif choice == '2':
            coding_problem()
        elif choice == '3':
            maths_quiz()
        elif choice == '4':
            games()

        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
