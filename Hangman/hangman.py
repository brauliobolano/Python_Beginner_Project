import random
import string
from words import words
from lives_visual_dict import lives_visual_dict

def get_valid_word(words):
    # Choose a random word from the list until it's valid (no '-' or spaces) and return it in uppercase
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    # Get a valid word and set up initial game variables
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase) 
    used_letters = set()
    lives = 7

    # Main game loop
    while len(word_letters) > 0 and lives > 0:
        print(f"\nWell, you still have {lives} lives")
        print(f"You have used the following letters: {''.join(used_letters)}")
        
        # Display hangman visual representation
        print(lives_visual_dict[lives])
        
        # Create a list showing guessed letters and placeholders for unguessed letters
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("\nCurrent word: ",''.join(word_list))

        # Get user's letter guess and convert it to uppercase
        user_letter = input("Guess one letter: ").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1  # Decrease lives if the guessed letter is not in the word
                print(f"\nSorry, {user_letter} is not in the word")
                print("\nYou lose one life")
        elif user_letter in used_letters:
            print("\nYou already used that letter. Don't make me take one of your lives.")
        else:
            print("\nThat's not a valid letter.")

    # Game over
    if lives == 0:
        print(f"\nThis is the end of the Journey, you have {lives} lives left")
    else:
        print(f"\nYou nailed it! Great Job, you still have {lives} lives. \n The Word is {word}.")

if __name__ == '__main__':
    hangman()
