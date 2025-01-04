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

    def Math_qiz():
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

        M_Q = input("Do you want to play again? (yes/no): ")
        if M_Q == 'yes':
            Math_qiz()
        else:
            print("Thanks for playing!")

    Math_qiz()


def games():
    while True:
        print("\nGaming section please select the game which you want to play")
        print("1. Guess the Number")
        print("2. Hangman")
        print("3. Rock, Paper, Scissors")
        print("4. Tic Tac Toe")
        print("5. Hand Cricket")
        print("6. Back to Main Menu")

        choice = input("Choose an option(1, 2, 3, 4, 5, 6): ")

        if choice == '1':
            guess_the_number()
        elif choice == '2':
            hangman()
        elif choice == '3':
            rock_paper_scissors()
        elif choice == '4':
            guess_the_number()
            # tic_tac_toe()
        elif choice == '5':
            hand_cricket()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def guess_the_number():
    print("Welcome to Guess the Number!")
    number = random.randint(1, 50)
    attempts = 0
    def guess():
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

        G_T_N = input("Do you want to play again? (yes/no): ").lower()
        if G_T_N == 'yes':
            guess_the_number()
        else:
            print("Thanks for playing!")

def hangman():
    stages = [
            '''
            ------
            |    |
            |
            |
            |
            |
            ''',
            '''
            ------
            |    |
            |    O
            |
            |
            |
            ''',
            '''
            ------
            |    |
            |    O
            |    |
            |
            |
            ''',
            '''
            ------
            |    |
            |    O
            |   /|
            |
            |
            ''',
            '''
            ------
            |    |
            |    O
            |   /|\\
            |
            |
            ''',
            '''
            ------
            |    |
            |    O
            |   /|\\
            |   /
            |
            ''',
            '''
                ------
                |    |
                |    O
                |   /|\\
                |   / \\
                |
            ''',
            ]

    word_dict = {
        "This is the color of the sky on a clear day": "blue",
        "It is a sweet fruit often associated with doctors": "apple",
        "A common pet that barks": "dog",
        "A type of transportation that flies in the sky": "plane",
        "The season that follows summer": "fall",
    }

    def hang_man():
        chosen_hint = random.choice(list(word_dict.keys()))
        chosen_word = word_dict[chosen_hint]
        word_length = len(chosen_word)
        
        lives = 6
        display = ['_'] * word_length

        print("word = ", display)
        print(chosen_hint)
        print(stages[0])  

        game_over = False

        while not game_over:
            guessed_letter = input("Guess a letter: ").lower()

            if guessed_letter in chosen_word:
                for position in range(word_length):
                    if chosen_word[position] == guessed_letter:
                        display[position] = guessed_letter
                print(f"Good job! '{guessed_letter}' is in the word.")
                print("word = ", display)
            else:
                lives -= 1
                print(f"Sorry! '{guessed_letter}' is not in the word.")
                print(f"You have {lives} lives left")
                print("word = ", display)
                print(stages[6 - lives])

            if lives == 0:
                print("You lose! The word was:", chosen_word)
                game_over = True
            elif '_' not in display:
                print("Congratulations! You win! The word is:", chosen_word)
                print(stages[0]) 
                game_over = True

        h_m = input("Do you want to play again? (yes/no): ").lower()
        if h_m == 'yes':
            hang_man()
        else:
            print("Thanks for playing!")
    hang_man()

def rock_paper_scissors():
    print("Let's play a game between you and the computer!")

    def R_P_S():
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

        r_p_s = input("Do you want to play again? (yes/no): ").lower()
        if r_p_s == 'yes':
            R_P_S()
        else:
            print("Thanks for playing!")

    R_P_S()

def tic_tac_toe():
    def T_T_T():       
        def sum(a, b, c):
            return a + b + c

        def printBoard(xState, zState):
            zero = 'X' if xState[0] else ('O' if zState[0] else 0)    
            one = 'X' if xState[1] else ('O' if zState[1] else 1)           
            two = 'X' if xState[2] else ('O' if zState[2] else 2)
            three = 'X' if xState[3] else ('O' if zState[3] else 3)
            four = 'X' if xState[4] else ('O' if zState[4] else 4)
            five = 'X' if xState[5] else ('O' if zState[5] else 5)
            six = 'X' if xState[6] else ('O' if zState[6] else 6)
            seven = 'X' if xState[7] else ('O' if zState[7] else 7)
            eight = 'X' if xState[8] else ('O' if zState[8] else 8)

            print(f"{zero} | {one} | {two}")
            print("--|---|--")
            print(f"{three} | {four} | {five}")
            print("--|---|--")
            print(f"{six} | {seven} | {eight}")


        def checkwin(xState, zState):
            wins = [
                [0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]
            ]
            
            for win in wins:
                if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
                    print("X Won the match")
                    return 1
                if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
                    print("O Won the match")
                    return 0

            return -1


        if __name__ == "__main__":
            xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]

            turn = 1 

            print("Welcome to Tic Tac Toe!")

            while True:
                printBoard(xState, zState)

                if turn == 1:
                    print("X's Chance")
                    value = int(input("Please enter a value (0-8): "))
                    if xState[value] == 0 and zState[value] == 0:
                        xState[value] = 1
                        turn = 0  
                    else:
                        print("Invalid move, try again.")
                else:
                    print("O's Chance")
                    value = int(input("Please enter a value (0-8): "))
                    if xState[value] == 0 and zState[value] == 0:
                        zState[value] = 1
                        turn = 1  
                    else:
                        print("Invalid move, try again.")

                cwin = checkwin(xState, zState)
                if cwin != -1:
                    print("Draw!!")
                
                t_t_t = input("Do you want to play again? (yes/no): ").lower()
                if t_t_t != "yes":
                    print("Thank you for playing!")
                    break
    T_T_T()

def hand_cricket():
    print("Let's play a game of Hand Cricket!")
    print("Note: You can only enter numbers between 1 and 6 as per the instructions.")
    def play_game():
        
        while True:
            option = int(input("Enter your option (1 for Batting, 2 for Bowling): "))
            if option not in [1, 2]:
                print("Invalid option. Please choose 1 for Batting or 2 for Bowling.")
                continue

            Num, a = 7, 81
            yourscore = 0
            computerscore = 0

            if option == 1:
                print("It's your batting first.")
                while a != Num:
                    a = int(input("Enter any number between 1-6: "))
                    if a not in range(1, 7):
                        print("Invalid input. Please enter a number between 1 and 6.")
                        continue
                    Num = random.randint(1, 6)
                    if a == Num:
                        print("You're out! Now it's the computer's turn.")
                        break
                    print("Good job!")
                    yourscore += a
                    print(f"Your option: {a}")
                    print(f"Computer's option: {Num}")
                    print(f"Your score: {yourscore}")
                
                Num, a = 7, 81
                print("Now it's your bowling.")
                while a != Num:
                    a = int(input("Enter any number between 1-6: "))
                    if a not in range(1, 7):
                        print("Invalid input. Please enter a number between 1 and 6.")
                        continue
                    Num = random.randint(1, 6)
                    if a == Num:
                        print("Good job! The computer is out.")
                        print(f"Computer's score: {computerscore}")
                        break
                    computerscore += Num
                    print(f"Your option: {a}")
                    print(f"Computer's option: {Num}")
                    print(f"Computer's score: {computerscore}")
                
                if yourscore > computerscore:
                    print("Congratulations! You win.")
                elif yourscore < computerscore:
                    print("You lose. Try next time.")
                else:
                    print("It's a draw.")

            elif option == 2:
                print("It's your bowling first.")
                while a != Num:
                    a = int(input("Enter any number between 1-6: "))
                    if a not in range(1, 7):
                        print("Invalid input. Please enter a number between 1 and 6.")
                        continue
                    Num = random.randint(1, 6)
                    if a == Num:
                        print("Good job! The computer is out.")
                        print(f"Computer's score: {computerscore}")
                        break
                    computerscore += Num
                    print(f"Your option: {a}")
                    print(f"Computer's option: {Num}")
                    print(f"Computer's score: {computerscore}")
                
                Num, a = 7, 81
                print("Now it's your batting.")
                while a != Num:
                    a = int(input("Enter any number between 1-6: "))
                    if a not in range(1, 7):
                        print("Invalid input. Please enter a number between 1 and 6.")
                        continue
                    Num = random.randint(1, 6)
                    if a == Num:
                        print("You're out! Now it's the computer's turn.")
                        break
                    print("Good job!")
                    yourscore += a
                    print(f"Your option: {a}")
                    print(f"Computer's option: {Num}")
                    print(f"Your score: {yourscore}")
                
                if yourscore > computerscore:
                    print("Congratulations! You win.")
                elif yourscore < computerscore:
                    print("You lose. Try next time.")
                else:
                    print("It's a draw.")

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thank you for playing!")
                break

    play_game()


        
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
