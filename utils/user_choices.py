
def get_user_choice():
    while True:
        try:
            option = int(input())
            return option
        except ValueError:
            print("Please enter a valid number!")


def get_user_continue_choice():
    while True:
        print("Continue?")
        print("[Y] Yes")
        print("[N] No")
        user_choice = str(input().lower())
        if user_choice in ["y", "n"]:
            return user_choice
        else:
            print("Please enter either 'Y' or 'N'!")