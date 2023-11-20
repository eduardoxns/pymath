from utils.menu_functions import menu_exponentiation_and_root
from utils.user_choices import get_user_choice, get_user_continue_choice


print("Welcome to the PyMath!")


def potentiation(a, b):
    response = a ** b
    print("The potentiation of the two numbers is equal to", response)


def root(a, b):
    response = a ** (1 / b)
    print("The rooting of the two numbers is equal to", response)


while True:
    menu_exponentiation_and_root()
    calculation = get_user_choice()

    while calculation not in [1, 2]:
        print("You need to choice one of four options!")
        menu_exponentiation_and_root()
        calculation = get_user_choice()
    try:
        num1 = int(input("Enter the base or root: "))
        num2 = int(input("Enter the exponent or index: "))
    except ValueError:
        print("Please enter valid numeric values for the numbers!")

    if calculation == 1:
        potentiation(num1, num2)
    elif calculation == 2:
        root(num1, num2)

    user_continue_choice = get_user_continue_choice()

    if user_continue_choice == "n":
        break
