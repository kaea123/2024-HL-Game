def int_checker(question, low=None, high=None, exit_code=None):

    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    # if the number needs to be between low & high
    else:
        error = (f"Please enter an integer that "
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if response is valid, return it
            return response

        except ValueError:
            print(error)


# Main Routine Starts here

# rounds = "test"
# while rounds != "":
#     rounds = int_checker("Rounds <enter> for infinite>: ", low=1, exit_code="")
#     print(f"You asked for {rounds}")

# low_num = int_checker("Low Number? ")
# print(f"You chose a low number of {low_num}")

# high_num = int_checker("High Number? ", low=1)
# print(f"You chose a high number of {high_num}")

# Check user guesses
guess = ""
while guess != "xxx":
    guess = int_checker("Guess: ", low=0, high=10, exit_code="xxx")
    print(f"you guessed {guess}")
    print()

