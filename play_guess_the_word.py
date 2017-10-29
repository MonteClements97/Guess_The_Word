def play_guess_the_word(the_word, lives):
    the_word = [letter.lower() for letter in the_word] # makes sure everything is lowercase
    secret_letters = ["_ "] * len(the_word)
    input("\"Let's start! Guess the first letter!\"")
    while lives != 0:
        print("".join(secret_letters))
        if "_ " in secret_letters:
            print("You have", lives, "remaining")
            users_guess = input("Enter letter:")
            if not(users_guess.lower() in the_word):
                print("\"That appears to be wrong! You've lost a life!")
                lives -= 1
            where_in_the_list = 0
            for letter in the_word:
                if letter.lower() == users_guess.lower():
                    secret_letters[where_in_the_list] = users_guess.lower() + ' '
                where_in_the_list += 1 # keep track of where we are in the list
        else:
            input("Congratulations, you have guessed the word!")



