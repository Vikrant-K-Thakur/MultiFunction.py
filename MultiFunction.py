
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
    def python_problem():
        dict_P = {
            "Program to Print Hello world!": '''print("Hello World!")''',
            "Program to find maximum of three numbers": '''a = int(input("Enter first number: "))\nb = int(input("Enter second number: "))\nc = int(input("Enter third number: "))\nif a > b and a > c:\n    print("First number is the greatest")\nelif b > a and b > c:\n    print("Second number is the greatest")\nelse:\n    print("Third number is the greatest")''',
            "Program to check if a year is leap": '''year = int(input("Enter a year: "))\nif year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):\n    print("Leap year")\nelse:\n    print("Not a leap year")''',
            "Program to find the area of a circle": '''r = float(input("Enter radius: "))\narea = 3.14 * r * r\nprint(f"Area of the circle: {area}")''',
            "Program to find the area of a triangle": '''b = float(input("Enter base: "))\nh = float(input("Enter height: "))\narea = 0.5 * b * h\nprint(f"Area of the triangle: {area}")''',
            "Program to display a number in reverse order": '''num = int(input("Enter a number: "))\nrev = 0\nwhile num > 0:\n    rev = rev * 10 + num % 10\n    num = num // 10\nprint(f"Reversed number: {rev}")'''
        }

        problem = random.choice(list(dict_P.keys()))
        solution = dict_P[problem]

        print(f"Problem: {problem}")
        show_solution = input("Do you want to see the solution? (yes/no): ").strip().lower()
        if show_solution == "yes":
            print(f"Solution:\n{solution}")
        continue_python = input("Do you want to continue with python problems? (yes/no): ").strip().lower()
        if continue_python == "yes":
            python_problem()

    def html_problem():
        dict_HTML = {
            "Create a simple HTML document": '''<!DOCTYPE html>\n<html>\n<head>\n    <title>Simple HTML</title>\n</head>\n<body>\n    <h1>Hello World!</h1>\n</body>\n</html>''',
            "Create a hyperlink": '''<a href=\"https://www.example.com\">Click Here</a>''',
            "Create an ordered list": '''<!DOCTYPE html>\n<html>\n<body>\n<ol>\n  <li>Item 1</li>\n  <li>Item 2</li>\n  <li>Item 3</li>\n</ol>\n</body>\n</html>''',
            "Create an unordered list": '''<!DOCTYPE html>\n<html>\n<body>\n<ul>\n  <li>Item 1</li>\n  <li>Item 2</li>\n  <li>Item 3</li>\n</ul>\n</body>\n</html>''',
            "Insert an image": '''<!DOCTYPE html>\n<html>\n<body>\n<img src=\"https://www.example.com/image.jpg\" alt=\"Example Image\" width=\"300\" height=\"200\">\n</body>\n</html>''',
            "Create a table": '''<!DOCTYPE html>\n<html>\n<body>\n<table border=\"1\">\n  <tr>\n    <th>Header 1</th>\n    <th>Header 2</th>\n  </tr>\n  <tr>\n    <td>Data 1</td>\n    <td>Data 2</td>\n  </tr>\n  <tr>\n    <td>Data 3</td>\n    <td>Data 4</td>\n  </tr>\n</table>\n</body>\n</html>''',
            "Embed a video": '''<!DOCTYPE html>\n<html>\n<body>\n<video width=\"320\" height=\"240\" controls>\n  <source src=\"movie.mp4\" type=\"video/mp4\">\n  Your browser does not support the video tag.\n</video>\n</body>\n</html>'''
        }
        problem, solution = random.choice(list(dict_HTML.items()))
        print(f"Problem: {problem}")
        show_solution = input("Do you want to see the solution? (yes/no): ").strip().lower()
        if show_solution == "yes":
            print(f"Solution:\n{solution}")
        continue_python = input("Do you want to continue with html problems? (yes/no): ").strip().lower()
        if continue_python == "yes":
            html_problem()

    def css_problem():
        dict_CSS = {
            "Change background color": '''body {\n    background-color: lightblue;\n}''',
            "Create a centered text": '''div {\n    text-align: center;\n    margin-top: 50px;\n}''',
            "Add border to an element": '''div {\n    border: 2px solid black;\n    padding: 10px;\n}''',
            "Create a hover effect": '''a:hover {\n    color: red;\n    text-decoration: underline;\n}''',
            "Style a button": '''button {\n    background-color: green;\n    color: white;\n    padding: 10px 20px;\n    border: none;\n    border-radius: 5px;\n    cursor: pointer;\n}''',
            "Make an image responsive": '''img {\n    max-width: 100%;\n    height: auto;\n}''',
            "Center an element vertically and horizontally": '''div {\n    display: flex;\n    justify-content: center;\n    align-items: center;\n    height: 100vh;\n}'''
        }
        problem, solution = random.choice(list(dict_CSS.items()))
        print(f"Problem: {problem}")
        show_solution = input("Do you want to see the solution? (yes/no): ").strip().lower()
        if show_solution == "yes":
            print(f"Solution:\n{solution}")
        continue_python = input("Do you want to continue with css problems? (yes/no): ").strip().lower()
        if continue_python == "yes":
            css_problem()

    def js_problem():
        dict_JS = {
            "Create a simple alert": '''alert("Hello World!");''',
            "Add two numbers": '''let a = prompt("Enter first number: ");\nlet b = prompt("Enter second number: ");\nalert("Sum: " + (parseInt(a) + parseInt(b)));''',
            "Change text of an element": '''document.getElementById("myElement").innerText = "Text has been changed!";''',
            "Hide an element on button click": '''document.getElementById("myButton").addEventListener("click", function() {\n    document.getElementById("myElement").style.display = "none";\n});''',
            "Validate an email address": '''function validateEmail(email) {\n    const regex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;\n    return regex.test(email);\n}\nalert(validateEmail("test@example.com"));''',
            "Generate a random number": '''let randomNumber = Math.floor(Math.random() * 100) + 1;\nalert("Random Number: " + randomNumber);''',
            "Toggle class on an element": '''document.getElementById("myElement").classList.toggle("active");'''
        }
        problem, solution = random.choice(list(dict_JS.items()))
        print(f"Problem: {problem}")
        show_solution = input("Do you want to see the solution? (yes/no): ").strip().lower()
        if show_solution == "yes":
            print(f"Solution:\n{solution}")
        continue_python = input("Do you want to continue with js problems? (yes/no): ").strip().lower()
        if continue_python == "yes":
            js_problem()

    def c_problem():
        dict_C = {
            "Print Hello World": '''#include <stdio.h>\nint main() {\n    printf("Hello World!\\n");\n    return 0;\n}''',
            "Find the sum of two numbers": '''#include <stdio.h>\nint main() {\n    int a, b;\n    printf("Enter two numbers: ");\n    scanf("%d %d", &a, &b);\n    printf("Sum: %d\\n", a + b);\n    return 0;\n}''',
            "Check if a number is even or odd": '''#include <stdio.h>\nint main() {\n    int num;\n    printf("Enter a number: ");\n    scanf("%d", &num);\n    if (num % 2 == 0)\n        printf("%d is even.\\n", num);\n    else\n        printf("%d is odd.\\n", num);\n    return 0;\n}''',
            "Find the factorial of a number": '''#include <stdio.h>\nint main() {\n    int n, i;\n    unsigned long long factorial = 1;\n    printf("Enter a positive integer: ");\n    scanf("%d", &n);\n    for (i = 1; i <= n; ++i) {\n        factorial *= i;\n    }\n    printf("Factorial of %d = %llu\\n", n, factorial);\n    return 0;\n}''',
            "Reverse a number": '''#include <stdio.h>\nint main() {\n    int num, reversed = 0, remainder;\n    printf("Enter an integer: ");\n    scanf("%d", &num);\n    while (num != 0) {\n        remainder = num % 10;\n        reversed = reversed * 10 + remainder;\n        num /= 10;\n    }\n    printf("Reversed number = %d\\n", reversed);\n    return 0;\n}''',
            "Check if a number is prime": '''#include <stdio.h>\nint main() {\n    int n, i, flag = 1;\n    printf("Enter a positive integer: ");\n    scanf("%d", &n);\n    if (n <= 1) {\n        flag = 0;\n    }\n    for (i = 2; i <= n / 2; ++i) {\n        if (n % i == 0) {\n            flag = 0;\n            break;\n        }\n    }\n    if (flag == 1)\n        printf("%d is a prime number.\\n", n);\n    else\n        printf("%d is not a prime number.\\n", n);\n    return 0;\n}''',
            "Find the largest of three numbers": '''#include <stdio.h>\nint main() {\n    int a, b, c;\n    printf("Enter three numbers: ");\n    scanf("%d %d %d", &a, &b, &c);\n    if (a >= b && a >= c)\n        printf("Largest number is %d\\n", a);\n    else if (b >= a && b >= c)\n        printf("Largest number is %d\\n", b);\n    else\n        printf("Largest number is %d\\n", c);\n    return 0;\n}'''
        }

        problem, solution = random.choice(list(dict_C.items()))
        print(f"Problem: {problem}")
        show_solution = input("Do you want to see the solution? (yes/no): ").strip().lower()
        if show_solution == "yes":
            print(f"Solution:\n{solution}")
        continue_python = input("Do you want to continue with c problems? (yes/no): ").strip().lower()
        if continue_python == "yes":
            c_problem()

    def cpp_problem():
        dict_CPP = {
            "Print Hello World": '''#include <iostream>\nusing namespace std;\nint main() {\n    cout << "Hello World!" << endl;\n    return 0;\n}''',
            "Find the largest of three numbers": '''#include <iostream>\nusing namespace std;\nint main() {\n    int a, b, c;\n    cout << "Enter three numbers: ";\n    cin >> a >> b >> c;\n    if (a > b && a > c)\n        cout << "First number is the greatest" << endl;\n    else if (b > a && b > c)\n        cout << "Second number is the greatest" << endl;\n    else\n        cout << "Third number is the greatest" << endl;\n    return 0;\n}''',
            "Check if a number is even or odd": '''#include <iostream>\nusing namespace std;\nint main() {\n    int num;\n    cout << "Enter a number: ";\n    cin >> num;\n    if (num % 2 == 0)\n        cout << num << " is even." << endl;\n    else\n        cout << num << " is odd." << endl;\n    return 0;\n}''',
            "Calculate factorial of a number": '''#include <iostream>\nusing namespace std;\nint main() {\n    int n;\n    unsigned long long factorial = 1;\n    cout << "Enter a positive integer: ";\n    cin >> n;\n    for (int i = 1; i <= n; ++i) {\n        factorial *= i;\n    }\n    cout << "Factorial of " << n << " = " << factorial << endl;\n    return 0;\n}''',
            "Reverse a number": '''#include <iostream>\nusing namespace std;\nint main() {\n    int num, reversed = 0, remainder;\n    cout << "Enter an integer: ";\n    cin >> num;\n    while (num != 0) {\n        remainder = num % 10;\n        reversed = reversed * 10 + remainder;\n        num /= 10;\n    }\n    cout << "Reversed number = " << reversed << endl;\n    return 0;\n}''',
            "Check if a number is prime": '''#include <iostream>\nusing namespace std;\nint main() {\n    int n, i;\n    bool isPrime = true;\n    cout << "Enter a positive integer: ";\n    cin >> n;\n    if (n <= 1) {\n        isPrime = false;\n    } else {\n        for (i = 2; i <= n / 2; ++i) {\n            if (n % i == 0) {\n                isPrime = false;\n                break;\n            }\n        }\n    }\n    if (isPrime)\n        cout << n << " is a prime number." << endl;\n    else\n        cout << n << " is not a prime number." << endl;\n    return 0;\n}''',
            "Swap two numbers using a temporary variable": '''#include <iostream>\nusing namespace std;\nint main() {\n    int a, b, temp;\n    cout << "Enter two numbers: ";\n    cin >> a >> b;\n    temp = a;\n    a = b;\n    b = temp;\n    cout << "After swapping: a = " << a << ", b = " << b << endl;\n    return 0;\n}'''
        }
        problem, solution = random.choice(list(dict_CPP.items()))
        print(f"Problem: {problem}")
        show_solution = input("Do you want to see the solution? (yes/no): ").strip().lower()
        if show_solution == "yes":
            print(f"\nSolution:\n{solution}")
        continue_python = input("\nDo you want to continue with c++ problems? (yes/no): \n").strip().lower()
        if continue_python == "yes":
            cpp_problem()

    problems = {
        1: ("Python", python_problem),
        2: ("HTML", html_problem),
        3: ("CSS", css_problem),
        4: ("JavaScript", js_problem),
        5: ("C", c_problem),
        6: ("C++", cpp_problem)
    }

    while True:
        print("\nWelcome to the Coding Problem Generator!")
        for key, (name, _) in problems.items():
            print(f"{key}. {name}")
        print("7. Exit")

        try:
            choice = int(input("Please select the language you want to solve the problem in: "))
            if choice == 7:
                print("Thank you for using the Coding Problem Generator!")
                break
            elif choice in problems:
                print(f"\nYou selected {problems[choice][0]}!")
                problems[choice][1]()
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")


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

        choice = input("Choose an option(1, 2, 3, 4, 5 or 6 for exit): ")

        if choice == '1':
            guess_the_number()
        elif choice == '2':
            hangman()
        elif choice == '3':
            rock_paper_scissors()
        elif choice == '4':
            tic_tac_toe()
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
        guess() 
    else:
        print("Thanks for playing!")
    guess()

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
        def printBoard(xState, zState):
            board = [
                'X' if xState[0] else ('O' if zState[0] else '0'),
                'X' if xState[1] else ('O' if zState[1] else '1'),
                'X' if xState[2] else ('O' if zState[2] else '2'),
                'X' if xState[3] else ('O' if zState[3] else '3'),
                'X' if xState[4] else ('O' if zState[4] else '4'),
                'X' if xState[5] else ('O' if zState[5] else '5'),
                'X' if xState[6] else ('O' if zState[6] else '6'),
                'X' if xState[7] else ('O' if zState[7] else '7'),
                'X' if xState[8] else ('O' if zState[8] else '8'),
            ]
            print(f"{board[0]} | {board[1]} | {board[2]}")
            print("--|---|--")
            print(f"{board[3]} | {board[4]} | {board[5]}")
            print("--|---|--")
            print(f"{board[6]} | {board[7]} | {board[8]}")

        def checkwin(xState, zState):
            wins = [
                [0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]
            ]
            
            for win in wins:
                if xState[win[0]] == 1 and xState[win[1]] == 1 and xState[win[2]] == 1:
                    return 1
                if zState[win[0]] == 1 and zState[win[1]] == 1 and zState[win[2]] == 1:
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
                else:
                    print("O's Chance")

                try:
                    value = int(input("Please enter a value (0-8): "))
                    if value < 0 or value > 8:
                        print("Invalid input. Please enter a number between 0 and 8.")
                        continue
                    if xState[value] == 0 and zState[value] == 0:
                        if turn == 1:
                            xState[value] = 1
                            turn = 0 
                        else:
                            zState[value] = 1
                            turn = 1  
                    else:
                        print("Invalid move, try again.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    continue

                cwin = checkwin(xState, zState)
                if cwin == 1:
                    printBoard(xState, zState)
                    print("X Won the match!")
                    break
                elif cwin == 0:
                    printBoard(xState, zState)
                    print("O Won the match!")
                    break
                elif all(xState[i] == 1 or zState[i] == 1 for i in range(9)):
                    printBoard(xState, zState)
                    print("It's a draw!")
                    break

            t_t_t = input("Do you want to play again? (yes/no): ").lower()
            if t_t_t == "yes":
                T_T_T()
            else:
                print("Thank you for playing!")

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


def To_Do_List():
    def to_do_list():
        print("Welcome to your to-do list!")
        print("You can add, delete, write and view tasks here.")

        pages = {}  # This is where pages (task lists) are stored.
        current_page = None  # Current selected page.

        def add_page():
            nonlocal pages
            page_name = f"Page {len(pages) + 1}"
            pages[page_name] = []
            print(f"Added {page_name}")

        def delete_page():
            nonlocal pages, current_page
            if not current_page:
                print("No page selected to delete!")
                return
            del pages[current_page]
            current_page = None
            print("Page deleted")

        def change_page():
            nonlocal pages, current_page
            if not pages:
                print("No pages available. Add a page first.")
                return

            print("Available Pages:")
            for idx, page in enumerate(pages.keys(), start=1):
                print(f"{idx}. {page}")

            try:
                choice = int(input("Select a page number: ")) - 1
                current_page = list(pages.keys())[choice]
                print(f"Switched to {current_page}")
            except (IndexError, ValueError):
                print("Invalid selection. Try again.")

        def add_task():
            nonlocal pages, current_page
            if not current_page:
                print("No page selected! Please select a page first.")
                return

            task = input("Enter task: ").strip()
            if task:
                pages[current_page].append({"task": task, "completed": False})
                print(f"Task '{task}' added to {current_page}")

        def mark_complete():
            nonlocal pages, current_page
            if not current_page:
                print("No page selected! Please select a page first.")
                return

            if not pages[current_page]:
                print("No tasks in this page!")
                return

            print("Tasks:")
            for idx, task in enumerate(pages[current_page], start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{idx}. {task['task']} - {status}")

            try:
                task_choice = int(input("Select task number to mark as complete: ")) - 1
                if 0 <= task_choice < len(pages[current_page]):
                    pages[current_page][task_choice]["completed"] = True
                    print("Task marked as complete.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid selection. Try again.")

        def show_status():
            nonlocal pages, current_page
            if not current_page:
                print("No page selected!")
                return

            all_tasks = len(pages[current_page])
            completed_tasks = sum(1 for task in pages[current_page] if task["completed"])

            if all_tasks == 0:
                print("No tasks in this page.")
            elif all_tasks == completed_tasks:
                print("Whole work is completed.")
            else:
                print(f"{completed_tasks} out of {all_tasks} tasks completed.")

        while True:
            print("\nTo-Do List Application")
            print("1. Add Page")
            print("2. Delete Page")
            print("3. Select Page")
            print("4. Add Task")
            print("5. Mark Task as Complete")
            print("6. Show Task Status")
            print("7. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                add_page()
            elif choice == "2":
                delete_page()
            elif choice == "3":
                change_page()
            elif choice == "4":
                add_task()
            elif choice == "5":
                mark_complete()
            elif choice == "6":
                show_status()
            elif choice == "7":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice! Please try again.")

        play_again1 = input("Do you want to continue? (yes/no): ").lower()
        if play_again1 == "yes":
            To_Do_List()
        elif play_again1 == "no":
            print("Thanks for playing")

    to_do_list()

def main():
    while True:
        print("\nPython Mobile Menu:")
        print("1. Calculator")
        print("2. Coding Problem")
        print("3. Maths Quiz")
        print("4. Games")
        print("5. To-Do List")
        print("6. Exit")
        choice = input("Choose an option(1, 2, 3, 4, 5 or 6 to exit): ")

        if choice == '1':
            calculator()
        elif choice == '2':
            coding_problem()
        elif choice == '3':
            maths_quiz()
        elif choice == '4':
            games()
        elif choice == '5':
            To_Do_List()

        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
