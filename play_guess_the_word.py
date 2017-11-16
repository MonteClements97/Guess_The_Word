def play_guess_the_word(the_word, lives):
    users_guesses = []
    the_word = list(the_word.lower())  # makes sure everything is lowercase
    secret_letters = ["_ "] * len(the_word)
    input("\"Let's start! Guess the first letter!\"")
    while lives != 0:
        print("".join(secret_letters))
        if "_ " in secret_letters:  # if there are still empty characters
            print("You have", lives, "lives remaining")
            print("Letters used: " + "".join(users_guesses))
            users_guess = input("Enter letter:")
            users_guess = users_guess.lower()
            if users_guess == '':  # nothing has been entered onto the keyboard
                print("\"You appeared to have entered nothing, try again\"")
            elif len(users_guess) > 1:
                print("\"You appeared to have entered", len(users_guess), "characters, you only need one!\"")
            elif users_guess + ' ' in users_guesses:
                print("\"You have already used that letter!\"")
            elif not users_guess.isalpha():
                print("\"Make sure you enter a letter!\"")
            elif not users_guess in the_word:  # the guess letter is not in the word
                users_guesses.append(users_guess + ' ')  # add the guess to collection of their guesses
                print("\"That appears to be wrong! You've lost a life!")
                lives -= 1
            else:
                users_guesses.append(users_guess + ' ')  # add the guess to collection of their guesses
                where_in_the_list = 0
                for letter in the_word:  # the letter must be in the word

                    if letter.lower() == users_guess:
                        secret_letters[where_in_the_list] = users_guess + ' '
                    where_in_the_list += 1  # keep track of where we are in the list
        else:
            input("Congratulations, you have guessed the word!")
            return
    input("You have run out of lives")
    return
