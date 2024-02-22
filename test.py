import random

def generate_random_number(length):
    return ''.join(random.choices('0123456789', k=length))

def display_word(word, guessed_letters):
    return ''.join(char if char in guessed_letters else '_' for char in word)

def draw_hangman(attempts):
    hangman_figures = [
        '''
           _______
          |/      |
          |      ( )
          |      /|\\
          |       |
          |      / \\
         _|_
        |   |______
        |          |
    ''',
    # Add more hangman figures for each incorrect guess
    ]

    return hangman_figures[attempts]

def hangman_game():
    random_number = generate_random_number(10)
    guessed_digits = set()
    max_attempts = 7
    attempts = 0
    game_won = False

    print("Welcome to Number Hangman!")
    print("Guess the random number. It contains 10 digits.")

    while attempts < max_attempts:
        print("\nNumber:", display_word(random_number, guessed_digits))
        print(draw_hangman(attempts))

        if set(random_number) == guessed_digits:
            game_won = True
            break

        guess = input("Guess a digit: ")

        if guess.isdigit() and len(guess) == 1:
            if guess in guessed_digits:
                print("You've already guessed that digit.")
            else:
                guessed_digits.add(guess)
                if guess not in random_number:
                    attempts += 1
                    print("Incorrect guess! Attempts left:", max_attempts - attempts)
                else:
                    print("Correct guess!")
        else:
            print("Please enter a single digit.")

    if game_won:
        print("Congratulations! You guessed the number:", random_number)
    else:
        print("Sorry, you've run out of attempts. The number was:", random_number)

hangman_game()
