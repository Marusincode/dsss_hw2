import random

def randomise_integer(min_value, max_value):
    """
    Randomising an integer in a specified range.

    Args:
        min_value (int): Minimum threshold for the integer
        max_value (int): Maximum threshold for the integer

    Returns:
        random integer between min_value and max_value (int) 

    """
    return random.randint(min_value, max_value)

#
def randomise_operator():
    """
    Randomising an operator for the math problem: +, -, or *.

    Args: none

    Returns:
        random operator between +, -, or * (str)

    """
    return random.choice(['+', '-', '*'])


def operation(number1, number2, operator):
    """
    Generating and solving n arithmetic problem.

    Args:
        number1 (int): First part of math problem
        number2 (int): Second part of math problem
        operator (str): Operator in the problem 

    Returns:
        problem (str): Generated problem
        answer (int): Answer to the problem

    """
    #forming a string that shows the problem
    problem = f"{number1} {operator} {number2}"

    #depending on operator, claculating the answer
    if operator == '+': answer = number1 + number2
    elif operator == '-': answer = number1 - number2
    else: answer = number1 * number2

    return problem, answer

def math_quiz():
    """
    Performing a math quiz based on generated problems and user input.

    Args: none

    Returns: none

    """

    #initial score is at 0, where is the chosen amount of problems is 3
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    #iterating through each problem
    for _ in range(total_questions):
        number1 = randomise_integer(1, 10); number2 = randomise_integer(1, 5); operator = randomise_operator()

        PROBLEM, ANSWER = operation(number1, number2, operator)
        print(f"\nQuestion: {PROBLEM}")
        
        #error handling for invalid input
        while True:
            try:
                useranswer = int(input("Your answer: "))
                break
            except ValueError:
                print("Your input is not valid. Please enter an integer")

        #checking if user's answer is correct and if they get a point
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    #presenting the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
