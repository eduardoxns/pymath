from utils.menu_functions import menu_basic_arithmetic_operations
from utils.user_choices import get_user_choice, get_user_continue_choice

print("Welcome to the PyMath!")


def addition(a, b):
    response = a + b
    print("The addition of the two numbers is equal to", response)


def subtraction(a, b):
    response = a - b
    print("The subtraction of the two numbers is equal to", response)


def multiplication(a, b):
    response = a * b
    print("The multiplication of the two numbers is equal to", response)


def division(a, b):
    try:
        response = a / b
        print("The division of the two numbers is equal to", response)
    except ZeroDivisionError:
        print("Error: Division by zero. Please enter a non-zero second number.")


while True:
    menu_basic_arithmetic_operations()
    calculation = get_user_choice()

    while calculation not in [1, 2, 3, 4]:
        print("You need to choice one of four options!")
        menu_basic_arithmetic_operations()
        calculation = get_user_choice()
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numeric values for the numbers!")

    if calculation == 1:
        addition(num1, num2)
    elif calculation == 2:
        subtraction(num1, num2)
    elif calculation == 3:
        multiplication(num1, num2)
    elif calculation == 4:
        division(num1, num2)

    user_continue_choice = get_user_continue_choice()

    if user_continue_choice == "n":
        break
