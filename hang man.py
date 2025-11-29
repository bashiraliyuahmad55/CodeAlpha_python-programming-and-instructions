import random

def hangman():
    """
    Simple text-based Hangman game.
    
    - Uses a list of 5 predefined words
    - Player guesses the word one letter at a time
    - Player has 6 incorrect guesses
    - Console input/output only
    """

    # 1. Predefined word list
    words = ["python", "river", "laptop", "school", "orange"]

    # 2. Randomly choose a word from the list
    word = random.choice(words)

    # 3. Create a list of underscores (_) representing unguessed letters
    guessed_word = ["_"] * len(word)

    # 4. Maximum allowed incorrect guesses
    attempts_left = 6

    # 5. Track letters the player already guessed
    guessed_letters = []

    print("===== HANGMAN GAME =====")
    print("Guess the word one letter at a time.")
    print("You have 6 incorrect guesses.\n")

    # Game loop continues while attempts remain
    while attempts_left > 0:
        print("Current word:", " ".join(guessed_word))
        print("Incorrect guesses left:", attempts_left)
        print("Guessed letters:", guessed_letters)

        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.\n")
            continue

        # Handle repeated guesses
        if guess in guessed_letters:
            print("You already guessed that letter!\n")
            continue

        # Add the guessed letter to the history
        guessed_letters.append(guess)

        # Correct guess
        if guess in word:
            print("Correct!\n")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print("Wrong guess!\n")
            attempts_left -= 1

        # Win condition
        if "_" not in guessed_word:
            print("\n🎉 Congratulations! You guessed the word:", word)
            return

    # If no attempts left → Game Over
    print("\n💀 Game Over! The correct word was:", word)


# Run the game
hangman()