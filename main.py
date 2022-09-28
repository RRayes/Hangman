import random
import string

from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def replay():
    play = input("would you like to play again? Y/N").upper()
    if play == 'Y':
        hangman()
    else:
        quit()

def win( word):
    print("Congratulations you have guessed the word: ", word)
    replay()

def loss(lives, word):
    if lives < 1:
        print("you have run out of lives. You Lose.")
        print("the word was ", word)
        replay()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 8

    while len(word_letters) > 0:

        loss(lives, word)
        print('The letters you have guess are', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("current lives: ", lives)
        print('current word:', ' '.join(word_list))
        user_letter = input('guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print("incorrect guess")
                lives -= 1
        elif user_letter in used_letters:
            print('You have already guessed this letter. try again')
        else:
            print('invalid character')
    win(word)

hangman()