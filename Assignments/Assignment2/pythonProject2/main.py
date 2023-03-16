# Lab Professor: Reza
# Ryan Lee | 101296633
import random
import operator
import math
from pathlib import Path

# PART A - MY MATH GAME
# Global variable Score that will be called on throughout the project
score = 0

# Function that generates a math question
def random_question():
    # Dictionary of operators, its string operator as the key
    # and the operator method as the value
    opDictionary = {'+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul}
    # Generate two numbers of range 1 - 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    # Randomly selects an operator from the operator dictionary
    op = random.choice(list(opDictionary.keys()))
    # formulates the mathematical expression and stores the answer in answer
    answer = opDictionary.get(op)(num1, num2)
    print('What is {} {} {}? \n '.format(num1, op, num2))
    return answer


# input validator for user to input an appropriate integer value
def get_valid_int():
    while True:
        try:
            guess = int(input("Enter Guess: "))
            return guess
        except ValueError:
            print("Invalid answer. Please try again.")


# input validator for user to put an appropriate float value
def get_valid_float(msg):
    while True:
        try:
            guess = float(input(msg))
            return guess
        except ValueError:
            print("Invalid answer. Please try again.")


# the math test function
def myMathTest():
    global score
    choice = 'y'
    score_file = Path("Score.txt")
    # conditional statement that checks if the Score.txt file exists
    if score_file.exists():
        f = open("Score.txt")
        prev_score = f.readline()
        f.close()
        print("I am happy to meet you again! Your last score was {}!,"
              " which {} is your saved score from the previous attempt.".format(prev_score, prev_score))
    else:
        print("Welcome to your Math Game!")
    # loop that loops indefinitely until user inputs anything other than 'Y'
    while choice.lower() == 'y':
        answer = random_question()
        guess = get_valid_int()
        # conditional statement that checks if the questions answer is correct
        if guess == answer:
            print("Congratulations! You are Pro!")
            score += 1
        else:
            print("The correct answer is {}. Let's try another question :)".format(answer))
            score -= 1
        # input that allows you to stay or leave the loop
        choice = input("Do you want to continue? (Y to continue, any other character to Exit) ")

        # conditional statement that writes or overwrites a Score.txt file with the score
        if choice.lower() != 'y':
            print("Thank you for playing!\nYou got {}!\nWOW!".format(score))
            f = open("Score.txt", 'w')
            f.write(str(score))
            f.close()


# PART B - The Quadratic Equation Game
# function that solves the descriminant of the equation
def descriminant(a, b, c):
    answer = b**2 - (4 * a * c)
    if answer > 0:
        x1 = (math.sqrt(answer) - b)/2 * a
        x2 = (math.sqrt(answer) + b)/2 * a
        print("We got two real solutions, which are {} and {}".format(x1, x2))
        f = open("QuadEqu.txt", "a")
        f.write("\nWe got two real solutions, which are {} and {}".format(x1, x2))
        f.close()
    elif answer == 0:
        x = b / (2 * a)
        print("We got one real solution, which is {}".format(x))
        f = open("QuadEqu.txt", "a")
        f.write("\nWe got one real solutions, which is {}".format(x))
        f.close()
    elif answer < 0:
        print("The Discriminant is negative, we got a pair of Complex solutions")
        f = open("QuadEqu.txt", "a")
        f.write("\nThe Descriminant is negative, we got a pair of Complex solutions")
        f.close()


# the quadratic equation test
def myQuadraticEquationTest():
    print("Welcome to the Quadratic Equation Game!\n"
          "Equation: aX^2 + bX + C = 0")
    a = get_valid_float("Please, enter the value for a: ")
    b = get_valid_float("Please, enter the value for b: ")
    c = get_valid_float("Please, enter the value for c: ")
    print("Your Quadratic Equation is: {}X^2 + {}X + {}". format(a, b, c))
    f = open("QuadEqu.txt", "w")
    f.write("Your Quadratic Equation is: {}X^2 + {}X + {}". format(a, b, c))
    f.close()
    descriminant(a, b, c)


myMathTest()
myQuadraticEquationTest()
