import random

def guess_number_game():
    target_number = random.randint(1, 10)

    while True:
        user_input = input("Guess a number between 1 and 10 (or type 'q' to quit): ")
        
        if user_input.lower() == 'q':
            print("Quitting the game. Goodbye!")
            break
        
        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
            continue

        if 1 <= guess <= 10:
            if guess == target_number:
                print("Congratulations! You guessed the right number!")
                break
            else:
                print("Wrong guess. Try again!")
        else:
            print("Please enter a number between 1 and 10.")
            
guess_number_game()
