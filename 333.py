import random

def main():
    country_list = [
        "Argentina", "Belgium", "China", "Denmark", "Egypt", "Finland",
        "Greece", "Hungary", "India", "Japan", "Kenya", "Luxembourg",
        "Mexico", "Netherlands", "Oman", "Poland", "Qatar", "Russia",
        "Spain", "Turkey", "Uganda", "Vietnam", "Yemen", "Zimbabwe"
    ]

    secret_country = random.choice(country_list).upper()

    def display_current_state(correct_guesses):
        displayed_word = ''.join([letter if letter in correct_guesses else '_' for letter in secret_country])
        print("Current state:", displayed_word)
        return displayed_word

    def process_guess(guess, correct_guesses, incorrect_guesses):
        guess = guess.upper()
        if guess in secret_country:
            print(f"Correct! The letter '{guess}' is in the word.")
            correct_guesses.add(guess)
            return True  
        else:
            print(f"Sorry, the letter '{guess}' is not in the word.")
            incorrect_guesses.add(guess)
            return False  

    def check_win(displayed_word):
        return '_' not in displayed_word

    correct_guesses = set()
    incorrect_guesses = set()
    chances = len(secret_country) + 2

    while chances > 0 and not check_win(display_current_state(correct_guesses)):
        guess = input("Please enter your guess (a single letter): ").strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetical character.")
            continue

        if guess.upper() in correct_guesses or guess.upper() in incorrect_guesses:
            print("You've already guessed that letter. Try a different one.")
            continue

        if not process_guess(guess, correct_guesses, incorrect_guesses):
            chances -= 1 
        
        if check_win(display_current_state(correct_guesses)):
            print("Congratulations! You've guessed the country correctly:", secret_country)
            return
        
        print(f"You have {chances} chances left.")

    if not check_win(display_current_state(correct_guesses)):
        print("You're out of chances. The secret country was:", secret_country)

if __name__ == "__main__":
    main()