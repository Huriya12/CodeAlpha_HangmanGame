# PYTHON PROGRAMMING TASK 1: THE HANGMAN GAME

# Random module to pick out a word from the list randomly
import random

# List of predefined words
words = ["apple", "banana", "mango", "orange", "pineapple"]

# Dictionary of Hangman ASCII drawings for each number of wrong guesses
hangman_frames = {0: ("  ",
                      "  ",
                      "  ",),

                  1: (" 0 ",
                      "  ",
                      "  ",),

                  2: (" 0 ",
                      " | ",
                      "  ",),

                  3: (" 0 ",
                      "/| ",
                      "  ",),

                  4: (" 0 ",
                      "/|\\",
                      "  ",),

                  5: (" 0 ",
                      "/|\\",
                      "/",),

                  6: (" 0 ",
                      "/|\\",
                      "/ \\",),}


def displayHangman(wrong_guesses):
    # Print the Hangman drawing corresponding to the current total of incorrect guesses
    print("=" * 40)
    for line in hangman_frames[wrong_guesses]:
        print(line)
    print("=" * 40)


def displayHint(hint):
    # Print the current progress (guessed letters are shown & unguessed letters are blank)
    print(" ".join(hint))


def displayAnswer(answer):
    # Print the complete word
    print(" ".join(answer))


def displayWelcome():
    # Print the welcome banner at the start of the program
    print("=" * 40)
    print("WELCOME TO THE HANGMAN GAME")
    print("=" * 40)


def displayInstructions():
    # Print the game rules and instructions
    print("\nHOW TO PLAY")
    print("- I'm thinking of a word, and you must guess it letter by letter.")
    print(f"- You have {len(hangman_frames) - 1} guesses before the game ends.")
    print("- Enter one letter at a time, just letters.")
    print("- Guess the whole word before the hangman is complete to win the game!\n")


def askReady():
    # Ask the player if they are ready to play the game
    # Keeps looping until a valid yes/no answer is given
    while True:
        response = input("Are you ready to start the game (yes/no): ").lower()

        # Returns True for 'yes' and False for 'no' to decide whether to continue the program or end it
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("Please enter 'yes' or 'no'")


def playGame():
    answer = random.choice(words)   # randomly pick a word
    hint = ["_"] * len(answer)  # blank placeholder for each letter
    wrong_guesses = 0   # count of incorrect guess
    guessed_letters = set() # tracker for letters that's been already guessed
    isRunning = True    # controls the game loop

    while isRunning:
        displayHangman(wrong_guesses)
        displayHint(hint)
        guess = input("Enter a letter: ").lower()

        # Invalidate user input if numerical value or a full word is answered
        # Ensure the input is one letter at a time only
        if len(guess) != 1 or not guess.isalpha():
            print("\n-------------------------------")
            print("| INVALID INPUT                |")
            print("| Please enter a single letter |")
            print("--------------------------------\n")
            continue

        # Prevent user from answering the same letter twice
        if guess in guessed_letters:
            print("\n------------------------")
            print("| ALREADY ANSWERED     |")
            print(f"| {guess} is already guessed |")
            print("------------------------\n")
            continue

        guessed_letters.add(guess)

        # If the guessed letter matches the word, it'll reveal it at every matching placement
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        # If the guessed letter is wrong, increase mistake count by 1
        else:
            wrong_guesses += 1

        # User win if every letter in the word has been guessed
        if "_" not in hint:
            displayHangman(wrong_guesses)
            displayAnswer(answer)
            print("\n-----------------------------")
            print("| Congratulations! You win! |")
            print("-----------------------------")
            isRunning = False
        # User lose if they ran out of attempts or chances 
        elif wrong_guesses >= len(hangman_frames) - 1:
            displayHangman(wrong_guesses)
            displayAnswer(answer)
            print("\n-----------------------------------")
            print("| You lose. Better luck next time |")
            print("-----------------------------------")
            isRunning = False


def askReplay():
    # Asks user if they want to play another round
    # Keeps looping until a valid yes/no response is given
    while True:
        response = input("\nWould you like to play the game again? (yes/no): ").lower()

        # Returns True for 'yes' and False for 'no' to decide whether to continue the program or end it
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("Please enter 'yes' or 'no'")


def main():
    # Display welcome banner, display instructions, and runs game loop (with replay option in the end)
    displayWelcome()
    
    if not askReady():
        print("Let's play maybe next time. Goodbye!")
        return

    displayInstructions()

    playing = True
    while playing:
        playGame()
        playing = askReplay()

    print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    main()