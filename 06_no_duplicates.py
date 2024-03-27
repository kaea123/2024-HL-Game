already_guessed =[]

secret = 7
guesses_used = 0
guesses_allowed = 5

guess = ""
while guess != secret:
    guess = int(input("Guess: "))

    # check that guess is not a duplicate
    if guess in already_guessed:
        print(f"You've already guessed {guess}.  You've *still* used "
              f"{guesses_used} / {guesses_allowed} guesses ")
        continue

    # if guess is not a duplicate, add it to the 'already guessed' list
    else:
        already_guessed.append(guess)

    guesses_allowed += 1