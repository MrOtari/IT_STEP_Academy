import random

# List of words for the game
word_list = ["python", "hangman", "program", "computer", "keyboard", "monitor", "mouse", "printer", "scanner"]

# Function to choose a random word from the list
def choose_word(word_list):
    return random.choice(word_list)

# Function to initialize the display word with underscores
def initialize_display_word(word):
    return "_" * len(word)

# Function to update the display word with correctly guessed letters
def update_display_word(word, display_word, letter):
    updated_display_word = ""
    for i in range(len(word)):
        if word[i] == letter:
            updated_display_word += letter
        else:
            updated_display_word += display_word[i]
    return updated_display_word

# Main function to run the Hangman game
def hangman():
    word = choose_word(word_list)
    display_word = initialize_display_word(word)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word. You have 6 attempts.")
    print(display_word)

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            display_word = update_display_word(word, display_word, guess)
            print(display_word)
            if "_" not in display_word:
                print("Congratulations! You guessed the word:", word)
                break
        else:
            attempts -= 1
            print("Incorrect guess. You have", attempts, "attempts left.")
            if attempts == 0:
                print("Sorry, you ran out of attempts. The word was:", word)
            else:
                print(display_word)

# Run the game
hangman()
